import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { VRButton } from 'three/addons/webxr/VRButton.js';
import * as Stats from 'three/addons/libs/stats.module.js';
import { GUI } from 'three/addons/libs/lil-gui.module.min.js';
//import { add } from 'three/examples/jsm/libs/tween.module.js';
import { ParametricGeometry } from 'three/addons/geometries/ParametricGeometry.js';

//////////////////////
/* GLOBAL VARIABLES */
//////////////////////
const resetRenderer = () => renderer.setSize(window.innerWidth, window.innerHeight);
const setupRenderer = () => { resetRenderer(); document.body.appendChild(renderer.domElement); renderer.xr.enabled = true; }
var perspectiveCam, auxCam, activeCamera, frontCamera;
var clock;
var scene, renderer, dirLight;
var carrossel, centerBase, smallRing, mediumRing, bigRing;
var objects = [];
var ringObjects = [];
const mats = {
    lambert: new THREE.MeshLambertMaterial({ color: Math.random() * 0xffffff, side: THREE.DoubleSide}),
    phong: new THREE.MeshPhongMaterial({ color: Math.random() * 0xffffff,   side: THREE.DoubleSide}),
    toon: new THREE.MeshToonMaterial({ color: Math.random() * 0xffffff ,  side: THREE.DoubleSide}),
    normal: new THREE.MeshNormalMaterial({side: THREE.DoubleSide}),
    basic: new THREE.MeshBasicMaterial({ color: Math.random() * 0xff0f00 ,  side: THREE.DoubleSide})
};

var mobiusLights = [];
var paramLights = [];

var geometry, mesh, material;
var shape, outerEllipse, innerEllipse, outerPoints, innerPoints, segments = 64;
var helperSmall, helperMedium, helperBig;

// For each ring
var parametricFunctions = [
    parametricSurface1, parametricSurface2, parametricSurface3, parametricSurface4,
    parametricSurface5, parametricSurface6, parametricSurface7, parametricSurface8
];
const numSurfaces = 8;
const angleStep = (2 * Math.PI) / numSurfaces;

/////////////////////
/* CREATE SCENE(S) */
/////////////////////
function createScene(){
    'use strict';

    scene = new THREE.Scene();
    //white background

    scene.background = new THREE.Color(0x000000);


    scene.add(new THREE.AxesHelper(10));

    createCarrossel(55, 0, 55);
    addSkydome(scene, 55, -10, 55);
    createLights();
}

//////////////////////
/* CREATE CAMERA(S) */
//////////////////////
function createCamera() {
    'use strict';

    perspectiveCam = new THREE.PerspectiveCamera(70,
                                         window.innerWidth / window.innerHeight,
                                         1,
                                         1000);

    auxCam = new THREE.OrthographicCamera(-100, 100, 100, -100, 1, 1000);

    frontCamera = new THREE.OrthographicCamera(-75, 75, 75, -40, 1, 1000);
    frontCamera.position.set(55, 30, 200);
    //auxCam = new THREE.StereoCamera();

    perspectiveCam.position.x = 100;
    perspectiveCam.position.y = 100;
    perspectiveCam.position.z = 100;

    auxCam.position.x = 55;
    auxCam.position.y = 125;
    auxCam.position.z = 55;


    perspectiveCam.lookAt(scene.position);
    //so para ser mais facil ver as cenas
    var controls = new OrbitControls(perspectiveCam, renderer.domElement);
    auxCam.lookAt(scene.position);
    activeCamera = frontCamera;
}

/////////////////////
/* CREATE LIGHT(S) */
/////////////////////
function createLights() {
    'use strict';

    const ambLight = new THREE.AmbientLight(0xffa500, 0.8);
    //scene.add(ambLight);

    dirLight = new THREE.DirectionalLight(0xffffff, 0.75);
    dirLight.position.set(70, 70, 70);
    dirLight.target.position.set(0, 35, 0);
    scene.add(dirLight);

    // helper = new THREE.DirectionalLightHelper(dirLight, 5);
    // scene.add(helper);
}

////////////////////////
/* CREATE OBJECT3D(S) */
////////////////////////
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Função para criar a faixa de Möbius
function createMobiusStrip(obj) {
    // Parâmetros para a faixa de Möbius
    const segments = 100;
    const radius = 1;
    const width = 0.2;

    // Arrays para vértices e índices
    const vertices = [];
    const indices = [];
    for (let i = 0; i <= segments; i++) {
        const t = (i / segments) * Math.PI * 2;
        const x1 = Math.cos(t) * (radius + width * Math.cos(t / 2));
        const y1 = Math.sin(t) * (radius + width * Math.cos(t / 2));
        const z1 = width * Math.sin(t / 2);

        const x2 = Math.cos(t) * (radius - width * Math.cos(t / 2));
        const y2 = Math.sin(t) * (radius - width * Math.cos(t / 2));
        const z2 = -width * Math.sin(t / 2);

        vertices.push(x1, y1, z1);
        vertices.push(x2, y2, z2);
    }

    for (let i = 0; i < segments; i++) {
        const a = 2 * i;
        const b = 2 * i + 1;
        const c = 2 * (i + 1);
        const d = 2 * (i + 1) + 1;

        // Adicionando as faces visíveis
        indices.push(a, b, d);
        indices.push(a, d, c);
    }

    const mobiusGeometry = new THREE.BufferGeometry();
    mobiusGeometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
    mobiusGeometry.setIndex(indices);
    mobiusGeometry.computeVertexNormals();

    // Criar a faixa de Möbius e adicionar à cena
    const mobiusMaterial = new THREE.MeshLambertMaterial({ color: 0x00ff00, side: THREE.DoubleSide });  // mats['lambert'];
    // mobiusMaterial.color = new THREE.Color(0x00ff00);
    const mobius = new THREE.Mesh(mobiusGeometry, mobiusMaterial);

    mobius.rotation.x = Math.PI / 2;
    mobius.position.set(0, 80, 0);
    mobius.scale.set(40, 40, 25);
    obj.add(mobius);
    objects.push(mobius);

    const lightPositions = [
        0, Math.PI / 4, Math.PI / 2, 3 * Math.PI / 4,
        Math.PI, 5 * Math.PI / 4, 3 * Math.PI / 2, 7 * Math.PI / 4
      ];

    lightPositions.forEach((t) => {
        const x = Math.cos(t) * (radius + width * Math.cos(t / 2));
        const y = Math.sin(t) * (radius + width * Math.cos(t / 2));
        const z = width * Math.sin(t / 2);

        const pointLight = new THREE.PointLight(0xffffff, 1000, 0);
        pointLight.position.set(x, y, z - 1.2);
        mobiusLights.push(pointLight);
        mobius.add(pointLight);
    });
}

function parametricSurface1(u, v, target) {
    // Cone
    const radius = 5 * (1 - v); // raio diminui com a altura
    const x = radius * Math.cos(2 * Math.PI * u);
    const y = 20 * (v - 0.5); //altura vai de -10 a 10
    const z = radius * Math.sin(2 * Math.PI * u);
    target.set(x, y, z);
}

function parametricSurface2(u, v, target) {
    // Trefoil Knot
    const scale = 2.5; // Scale factor to increase the size of the shape

    u *= 2 * Math.PI; // u ranges from 0 to 2 * Math.PI
    v *= 2 * Math.PI; // v ranges from 0 to 2 * Math.PI

    const x = scale * (Math.sin(u) + 2 * Math.sin(v));
    const y = scale * (Math.cos(u) - 2 * Math.cos(v));
    const z = scale * (-Math.sin(2 * u) + Math.sin(2 * v));

    target.set(x, y, z);
}

function parametricSurface3(u, v, target) {
    // cilindros cortados ao meio
    const tubeRadius = 5; // Radius of the tube
    const tubeHeight = 20; // Height of the tube

    // Calculate x, y, and z coordinates based on u, v parameters
    const theta = u * Math.PI * 2; // Angle around the tube
    const x = Math.cos(theta) * tubeRadius; // Calculate x-coordinate using cosine function
    const y = Math.sin(theta) * tubeRadius; // Calculate y-coordinate using sine function
    const z = (v - 0.5) * tubeHeight; // Map v parameter to height of the tube

    // Set the target vector with the calculated coordinates
    target.set(x, y, z);
}

function parametricSurface4(u, v, target) {
    // Curvas
    const x = Math.sin(u * Math.PI) * 5;
    const y = Math.cos(v * Math.PI) * 5;
    const z = u * 20 - 10;
    target.set(x, y, z);
}

function parametricSurface5(u, v, target) {
    // Vs
    const x = Math.sin(u * Math.PI) * 15;
    const y = Math.sin(v * Math.PI) * 15;
    const z = u * 10 - 5;
    target.set(x, y, z);
}

function parametricSurface6(u, v, target) {
    // Planos
    u *= Math.PI; // u ranges from 0 to Pi
    v *= 2 * Math.PI; // v ranges from 0 to 2*Pi

    let x, y, z;
    if (u < Math.PI) {
        x = 3 * Math.cos(u) * (1 + Math.sin(u)) + (2 * (1 - Math.cos(u) / 2)) * Math.cos(u) * Math.cos(v / 2);
        y = 8 * Math.sin(u) + (2 * (1 - Math.cos(u) / 2)) * Math.sin(u) * Math.cos(v / 2);
    } else {
        x = 3 * Math.cos(u) * (1 + Math.sin(u)) + (2 * (1 - Math.cos(u) / 2)) * Math.cos(v / 2 + Math.PI);
        y = 8 * Math.sin(u);
    }
    z = (2 * (1 - Math.cos(u) / 2)) * Math.sin(v / 2);

    target.set(x, y, z);
}

function parametricSurface7(u, v, target) {
    const scale = 8;  // Scale factor to increase the size of the shape
    // Planos
    const a = 1, b = 1, m = 4, n1 = 7, n2 = 2, n3 = 3;

    // Convert u, v to spherical coordinates
    const phi = u * 2 * Math.PI;
    const theta = v * Math.PI;

    const r = Math.sin(m * phi / 2) ** n2 + Math.cos(n1 * theta / 2) ** n3;
    const x = scale * r * Math.sin(theta) * Math.cos(phi);
    const y = scale * r * Math.sin(theta) * Math.sin(phi);
    const z = scale * r * Math.cos(theta);

    target.set(x, y, z);
}

function parametricSurface8(u, v, target) {
    const scale = 5; // Scale factor to increase the size of the shape
    const a = 1;
    const b = 0.2;

    u *= 2 * Math.PI; // u ranges from 0 to 2 * Math.PI
    v *= 2; // v ranges from 0 to 2

    const x = scale * Math.cos(u) * Math.sin(v);
    const y = scale * Math.sin(u) * Math.sin(v);
    const z = scale * (Math.cos(v) + Math.log(Math.tan(v / 2))) + scale * Math.cos(v) * Math.cos(u);

    target.set(x, y, z);
}

function addSmallParametricSurfaces(radius, z, parametricFunctions) {

    for (let i = 0; i < numSurfaces; i++) {
        const angle = i * angleStep;
        const x = radius * Math.cos(angle);
        const y = radius * Math.sin(angle);

        // Create geometry using one of the parametric functions
        const geometry = new ParametricGeometry(parametricFunctions[i]); // , 5, 5);
        const material = new THREE.MeshLambertMaterial({ color: Math.random() * 0xffffff, side: THREE.DoubleSide }); // new THREE.MeshBasicMaterial({ color: Math.random() * 0xffffff, side: THREE.DoubleSide, wireframe: false });
        const surface = new THREE.Mesh(geometry, material);
        
        // Randomize scale
        surface.scale.set(
            /* Math.random() * */ 0.3, 
            /* Math.random() * */ 0.3,  
            /* Math.random() * */ 0.3
        );
        
        // Set position
        surface.position.set(x, y, z - 28);
        // Scale the surface
        // surface.scale.set(0.3, 0.3, 0.3);
        surface.scale.set(0.4, 0.4, 0.4);

        // Randomize rotation
        surface.rotation.x = Math.random() * Math.PI;
        surface.rotation.y = Math.random() * Math.PI;
        surface.rotation.z = Math.random() * Math.PI;

        // Add surface to the object
        objects.push(surface);
        ringObjects.push(surface);
        smallRing.add(surface);

        // Add SpotLight to the surface
        const spotLightSmall = new THREE.SpotLight(0xffffff, 120, 10, Math.PI/4, 0.25);
        spotLightSmall.position.set(x, y, z - 22.8);
        spotLightSmall.target.position.set(0, 150, 0);
        paramLights.push(spotLightSmall);
        smallRing.add(spotLightSmall);

        helperSmall = new THREE.SpotLightHelper(spotLightSmall);
        // scene.add(helperSmall);
    }
}

function addMediumParametricSurfaces(radius, z, parametricFunctions) {

    for (let i = 0; i < numSurfaces; i++) {
        const angle = i * angleStep;
        const x = radius * Math.cos(angle);
        const y = radius * Math.sin(angle);

        // Create geometry using one of the parametric functions
        const geometry = new ParametricGeometry(parametricFunctions[i]); // , 5, 5);
        const material = new THREE.MeshLambertMaterial({ color: Math.random() * 0xffffff , side: THREE.DoubleSide});
        const surface = new THREE.Mesh(geometry, material);
        
        // Randomize scale
        surface.scale.set(0.5, 0.5, 0.5);
        
        // Set position
        surface.position.set(x, y, z - 26);
        // Scale the surface
        // surface.scale.set(0.5, 0.5, 0.5);
        // surface.scale.set(0.3, 0.3, 0.3);
        surface.scale.set(0.4, 0.4, 0.4);


        // Randomize rotation
        surface.rotation.x = Math.random() * Math.PI;
        surface.rotation.y = Math.random() * Math.PI;
        surface.rotation.z = Math.random() * Math.PI;

        // Add surface to the object
        objects.push(surface);
        ringObjects.push(surface);
        mediumRing.add(surface);

        const spotLightMedium = new THREE.SpotLight(0xffffff, 190, 20, Math.PI/4, 0.25);
        spotLightMedium.position.set(x, y, z - 16);
        spotLightMedium.target.position.set(0, 190, 0);
        paramLights.push(spotLightMedium);
        mediumRing.add(spotLightMedium);

        helperMedium = new THREE.SpotLightHelper(spotLightMedium);
        // scene.add(helperMedium);
    }
}

function addBigParametricSurfaces(radius, z, parametricFunctions) {

    for (let i = 0; i < numSurfaces; i++) {
        const angle = i * angleStep;
        const x = radius * Math.cos(angle);
        const y = radius * Math.sin(angle);

        // Create geometry using one of the parametric functions
        const geometry = new ParametricGeometry(parametricFunctions[i]); // , 5, 5);
        const material = new THREE.MeshLambertMaterial({ color: Math.random() * 0xffffff , side: THREE.DoubleSide});
        const surface = new THREE.Mesh(geometry, material);
        
        // Randomize scale
        surface.scale.set(0.65, 0.65, 0.65);
        
        // Set position
        surface.position.set(x, y, z - 22);
        // Scale the surface
        // surface.scale.set(0.5, 0.5, 0.5);
        surface.scale.set(0.3, 0.3, 0.3);

        // Randomize rotation
        surface.rotation.x = Math.random() * Math.PI;
        surface.rotation.y = Math.random() * Math.PI;
        surface.rotation.z = Math.random() * Math.PI;

        // Add surface to the object
        objects.push(surface);
        ringObjects.push(surface);
        bigRing.add(surface);

        const spotLightBig = new THREE.SpotLight(0xffffff, 240, 20, Math.PI/8, 0.25);
        spotLightBig.position.set(x, y, z - 10);
        spotLightBig.target.position.set(0, 250, 0);
        paramLights.push(spotLightBig);
        bigRing.add(spotLightBig);

        helperBig = new THREE.SpotLightHelper(spotLightBig);
        // scene.add(helperBig);
    }
}


/*
function addParametricSurfaces(obj, radius, y, parametricFunctions) {
    const numSurfaces = 8;
    const angleStep = (2 * Math.PI) / numSurfaces;
    
    for (let i = 0; i < numSurfaces; i++) {
        const angle = i * angleStep;
        const x = radius * Math.cos(angle);
        const z = radius * Math.sin(angle);
        
        // Create geometry using one of the parametric functions
        const geometry = new ParametricGeometry(parametricFunctions[i]); // , 5, 5);
        const material = new THREE.MeshBasicMaterial({ color: Math.random() * 0xffffff, side: THREE.DoubleSide, wireframe: false });
        const surface = new THREE.Mesh(geometry, material);
        
        // Randomize scale
        surface.scale.set(
            Math.random() * 0.5 + 0.5, 
            Math.random() * 0.5 + 0.5,  
            Math.random() * 0.5 + 0.5
        );
        
        // Set position
        surface.position.set(x - 3, y - 25, z - 6);
        
        // Randomize rotation
        surface.rotation.x = Math.random() * Math.PI;
        surface.rotation.y = Math.random() * Math.PI;
        surface.rotation.z = Math.random() * Math.PI;
        
        
        // Add surface to the object
        obj.add(surface);
    }
}
*/

function aux_createRingShape(innerRadius, outerRadius) {
    'use strict';
    const shape = new THREE.Shape();

    const outerEllipse = new THREE.EllipseCurve(
        0, 0, // center
        outerRadius, outerRadius, // largura e altura da elipse (iguais para ser curva perfeita)
        0, Math.PI * 2, // Angulo inicial e final (360º) 
        false, // 
        segments // segments for smoothness
    );
    const outerPoints = outerEllipse.getPoints(segments);
    shape.moveTo(outerPoints[0].x, outerPoints[0].y);

    for (let i = 1; i < segments; i++) {
        shape.lineTo(outerPoints[i].x, outerPoints[i].y);
    }

    const innerEllipse = new THREE.EllipseCurve(
        0, 0, // center
        innerRadius, innerRadius, // largura e altura da elipse (iguais para ser curva perfeita)
        0, Math.PI * 2, // Angulo inicial e final (360º) 
        false, 
        segments // segments for smoothness
    );
    const innerPoints = innerEllipse.getPoints(segments);
    shape.holes.push(new THREE.Path().moveTo(innerPoints[0].x, innerPoints[0].y).absarc(0, 0, innerRadius, 0, Math.PI * 2, true));

    return shape;
}

function addSkydome(obj, x, y, z) {
    'use strict';
    
    // Criar a calote esférica (skydome)
    var skyGeometry = new THREE.SphereGeometry(200, 32, 32, 0, Math.PI * 2, 0, Math.PI / 2);
    var textureLoader = new THREE.TextureLoader();
    var skyTexture = textureLoader.load('fischinger_frame.jpg');
    var skyMaterial = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        map: skyTexture,
        side: THREE.BackSide
    });
    var skydome = new THREE.Mesh(skyGeometry, skyMaterial);
    skydome.position.set(x, y, z);
    obj.add(skydome);
}   

function addCenterBase(obj, x, y, z) {
    'use strict';
    
    // // Caminho linear para o cilindro
    // var path = new THREE.LineCurve3(
    //     new THREE.Vector3(0, -30, 0),
    //     new THREE.Vector3(0, 40, 0)
    //     //altura do cilindro 70
    // );

    // geometry = new THREE.TubeGeometry(path, 40, 5, 16, true);

    geometry = new THREE.CylinderGeometry(5, 5, 70, 64);
    centerBase = new THREE.Mesh(geometry, mats['lambert']);
    centerBase.position.set(x, y + 35, z);
    obj.add(centerBase);
    objects.push(centerBase);
}

function addSmallRing(obj, x, y, z) {
    'use strict';
    shape = aux_createRingShape(5, 13);
    const extrudeOptions = {
        depth: 5, // ring thickness
        bevelEnabled: false,
      };

    geometry = new THREE.ExtrudeGeometry(shape, extrudeOptions);

    smallRing = new THREE.Mesh(geometry, mats['lambert']);
    smallRing.position.set(x, y, z);
    smallRing.rotation.x = Math.PI / 2;

    smallRing.userData = {up: false, do: false};
    parametricFunctions = shuffle(parametricFunctions);
    addSmallParametricSurfaces(9, 22, parametricFunctions); // For small ring

    obj.add(smallRing);
    objects.push(smallRing);
    smallRing.userData = {up: false, down: false};

}

function addMediumRing(obj, x, y, z) {
    'use strict';
    shape = aux_createRingShape(13, 21);
    const extrudeOptions = {
        depth: 5, // ring thickness
        bevelEnabled: false,
      };
  
    geometry = new THREE.ExtrudeGeometry(shape, extrudeOptions);

    mediumRing = new THREE.Mesh(geometry, mats['lambert']);
    mediumRing.position.set(x, y, z);
    mediumRing.rotation.x = Math.PI / 2;
    parametricFunctions = shuffle(parametricFunctions);
    addMediumParametricSurfaces(17, 16, parametricFunctions); // For medium ring

    obj.add(mediumRing);
    objects.push(mediumRing);
    mediumRing.userData = {up: false, down: false};

}

function addBigRing(obj, x, y, z) {
    'use strict';
    shape = aux_createRingShape(21, 29);
    const extrudeOptions = {
        depth: 5, // ring thickness
        bevelEnabled: false,
      };

    geometry = new THREE.ExtrudeGeometry(shape, extrudeOptions);

    bigRing = new THREE.Mesh(geometry, mats['lambert']);
    bigRing.position.set(x, y, z);
    bigRing.rotation.x = Math.PI / 2;
    parametricFunctions = shuffle(parametricFunctions);
    addBigParametricSurfaces(25, 10, parametricFunctions); // For big ring

    obj.add(bigRing);
    objects.push(bigRing);
    bigRing.userData = {up: false, down: false};
}

function createCarrossel(x, y, z) {
    'use strict';

    carrossel = new THREE.Object3D();

    addCenterBase(carrossel, 0, 0, 0);
    addSmallRing(carrossel, 0, 5, 0);  // antes: y = 17
    addMediumRing(carrossel, 0, 5, 0); // antes: y = 11
    addBigRing(carrossel, 0, 5, 0);
    createMobiusStrip(carrossel);
    scene.add(carrossel);

    carrossel.position.set(x, y, z);
}


//////////////////////
/* CHECK COLLISIONS */
//////////////////////
function checkCollisions(){
    'use strict';

}

///////////////////////
/* HANDLE COLLISIONS */
///////////////////////
function handleCollisions(){
    'use strict';

}

////////////
/* UPDATE */
////////////
function update(){
    'use strict';

    var delta = clock.getDelta();

    if (smallRing.userData.up) {
        if (smallRing.position.y < 70)  
            smallRing.position.y += 10 * delta;
    }

    if (smallRing.userData.down) {
        if (smallRing.position.y > 5)  // antes: y > 17
        smallRing.position.y -= 10 * delta;
    }

    if (mediumRing.userData.up) {
        if (mediumRing.position.y < 70) // antes: y < 64
            mediumRing.position.y += 10 * delta;
    }
    
    if (mediumRing.userData.down) {
        if (mediumRing.position.y > 5) // antes: y > 11
            mediumRing.position.y -= 10 * delta;
    }

    if (bigRing.userData.up) {
        if (bigRing.position.y < 70)    // antes: y < 58
            bigRing.position.y += 10 * delta;
    }

    if (bigRing.userData.down) {
        if (bigRing.position.y > 5)
            bigRing.position.y -= 10 * delta;
    }
}

/////////////
/* DISPLAY */
/////////////
function setMaterial(type) {
    for (var i = 0; i < objects.length; i++) {
        objects[i].material = mats[type];
    }
}

let lightingEnabled = true;

function toggleLighting() {
    lightingEnabled = !lightingEnabled;
    if (lightingEnabled) {
        renderer.physicallyCorrectLights = true;
    } else {
        renderer.physicallyCorrectLights = false;
    }
}

function toggleLightingMobius() {
    for (let i = 0; i < mobiusLights.length; i++) {
        mobiusLights[i].visible = !mobiusLights[i].visible;
    }
}

function toggleLightingParametric() {
    for (let i = 0; i < paramLights.length; i++) {
        paramLights[i].visible = !paramLights[i].visible;
    }

}

function render() {
    'use strict';

    renderer.render(scene, activeCamera);
}

////////////////////////////////
/* INITIALIZE ANIMATION CYCLE */
////////////////////////////////
function init() {
    'use strict';

    renderer = new THREE.WebGLRenderer({
        antialias: true
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // VR
    document.body.appendChild( VRButton.createButton( renderer ) );
    renderer.xr.enabled = true;
    renderer.setAnimationLoop( function () { renderer.render( scene, camera ); } );
    // VR
    
    createScene();
    createCamera();

    clock = new THREE.Clock();

    render();

    window.addEventListener("resize", onResize);
    document.addEventListener("keydown", onKeyDown);
    document.addEventListener("keyup", onKeyUp);
}

/////////////////////
/* ANIMATION CYCLE */
/////////////////////
function animate() {
    'use strict';

    update();

    render();

    // Rotação do carrossel
    carrossel.rotation.y += 0.01;

    //Rotação dos objetos dos anéis
    for (let i = 0; i < numSurfaces * 3; i++) {
        ringObjects[i].rotation.y += 0.05;
    }

    // Update da posição dos helpers das spotlights
    // helperSmall.update();
    // helperMedium.update();
    // helperBig.update();
}

////////////////////////////
/* RESIZE WINDOW CALLBACK */
////////////////////////////
function onResize() { 
    'use strict';

    renderer.setSize(window.innerWidth, window.innerHeight);

    if (window.innerHeight > 0 && window.innerWidth > 0) {
        perspectiveCam.aspect = window.innerWidth / window.innerHeight;
        perspectiveCam.updateProjectionMatrix();
    }

}

///////////////////////
/* KEY DOWN CALLBACK */
///////////////////////
function onKeyDown(e) {
    'use strict';
    switch (e.keyCode) {
        case 53: // 5
            activeCamera = perspectiveCam;
            break;
        case 54: // 6
            activeCamera = auxCam;
            break;
        case 55: // 7
            activeCamera = frontCamera;
            break;
        case 81: // Q
            setMaterial('lambert');
            break;
        case 87: // W
            setMaterial('phong');
            break;
        case 69: // E
            setMaterial('toon');
            break;
        case 82: // R
            setMaterial('normal');
            break;
        case 84: // T
            setMaterial('basic');
            break;
        case 68: // D
            dirLight.visible = !dirLight.visible;
            break;
        case 83: //S
            toggleLightingParametric();
            break;
        case 80: //P
            toggleLightingMobius();
            break;
        case 49: // 1
            smallRing.userData.up = true;
            smallRing.userData.down = false;
            break;
        case 50: // 2
            mediumRing.userData.up = true;
            mediumRing.userData.down = false;
            break;
        case 51: // 3
            bigRing.userData.up = true;
            bigRing.userData.down = false;
            break;
    }
}

///////////////////////
/* KEY UP CALLBACK */
///////////////////////
function onKeyUp(e){
    'use strict';

    switch(e.keyCode){
        case 49: // 1
            smallRing.userData.up = false;
            smallRing.userData.down = true;
            break;
        case 50: // 2
            mediumRing.userData.up = false;
            mediumRing.userData.down = true;
            break;
        case 51: // 3
            bigRing.userData.up = false;
            bigRing.userData.down = true;
            break;
    }
}

init();
renderer?.setAnimationLoop(animate);