import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { VRButton } from 'three/addons/webxr/VRButton.js';
import * as Stats from 'three/addons/libs/stats.module.js';
import { GUI } from 'three/addons/libs/lil-gui.module.min.js';

//////////////////////
/* GLOBAL VARIABLES */
//////////////////////
var crane, lanca, car;
var movementBool;
var base, tower, rotator, cabine, portaLanca, _lanca, contraLanca, contraPeso, cabos1, tirante1, tirante2, tirante3, tirante4;
var baseGarra, Garra, hook1, hook2, hook3, hook4;
var Contentor;

var frontCamera, sideCamera, topCamera, sceneCamera1, sceneCamera2, mobileCamera;
var activeCamera;
var scene, renderer, clock;
var geometry, material, material2, material3, materials = [];

var objeto1, objeto2, objeto3, objeto4, objeto5;
var objetos = [];

/////////////////////
/* CREATE SCENE(S) */
/////////////////////
function addBase(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(9, 3, 9);
    base = new THREE.Mesh(geometry, material);
    base.position.set(x, y + 2, z);
    obj.add(base);
}

function addTower(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 20, 2);
    tower = new THREE.Mesh(geometry, material);
    tower.position.set(x, y, z);
    obj.add(tower);
}

function addCabine(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 4, 4);
    cabine = new THREE.Mesh(geometry, material2);
    cabine.position.set(x, y, z);
    obj.add(cabine);
}

function addRotator(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 1, 2);
    rotator = new THREE.Mesh(geometry, material2);
    rotator.position.set(x, y, z);
    obj.add(rotator);
}

function addPortaLanca(obj, x, y, z) {
    'use strict';

    geometry = new THREE.ConeGeometry(1.8, 7, 4);
    portaLanca = new THREE.Mesh(geometry, material2);
    portaLanca.position.set(x, y, z);

    // Defina o ângulo de rotação da base do cone
    var angleInRadians = Math.PI / 4; // um quarto de volta (45 graus) em radianos
    portaLanca.rotation.y = angleInRadians;

    obj.add(portaLanca);
}

function addLanca(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 2, 20);
    _lanca = new THREE.Mesh(geometry, material2);
    _lanca.position.set(x, y + 2, z - 11);
    obj.add(_lanca);
}

function addContraLanca(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 2, 14);
    contraLanca = new THREE.Mesh(geometry, material2);
    contraLanca.position.set(x, y + 2, z + 8);
    obj.add(contraLanca);
}

function addContraPeso(obj, x, y, z) {
    'use strict';

    geometry = new THREE.BoxGeometry(2, 5, 3);
    contraPeso = new THREE.Mesh(geometry, material2);
    contraPeso.position.set(x, y + 2, z + 10);
    obj.add(contraPeso);
}

function addCabos(obj, x, y, z) {
    'use strict';
    
    geometry = new THREE.BoxGeometry(0.2, 15, 0.2);
    cabos1 = new THREE.Mesh(geometry, material3);
    cabos1.position.set(x , y + 2, z + 5);
    obj.add(cabos1);
}

function addTirantes(obj, x, y, z) {
    'use strict';
    
    geometry = new THREE.BoxGeometry(0.2, 10, 0.2);
    
    tirante1 = new THREE.Mesh(geometry, material2);
    tirante1.position.set(x - 0.5, y + 14, z - 4);
    tirante1.rotation.x = Math.PI / 3;
    tirante1.rotation.z = - Math.PI / 30;

    tirante2 = new THREE.Mesh(geometry, material2);
    tirante2.position.set(x + 0.5, y + 14, z - 4);
    tirante2.rotation.x = Math.PI / 3;
    tirante2.rotation.z = Math.PI / 30;

    tirante3 = new THREE.Mesh(geometry, material2);
    tirante3.position.set(x - 0.5, y + 14, z + 4);
    tirante3.rotation.x = - Math.PI / 3;
    tirante3.rotation.z = - Math.PI / 30;

    tirante4 = new THREE.Mesh(geometry, material2);
    tirante4.position.set(x + 0.5, y + 14, z + 4);
    tirante4.rotation.x = - Math.PI / 3;
    tirante4.rotation.z = Math.PI / 30;

    obj.add(tirante1);
    obj.add(tirante2);
    obj.add(tirante3);
    obj.add(tirante4);
}

function addGarra(x, y, z) {
    'use strict';

    baseGarra = new THREE.Mesh(new THREE.CylinderGeometry(1, 1, 0.5, 20), material3);
    baseGarra.rotation.y = Math.PI / 2;
    baseGarra.position.set(x, y - 5.5, z + 5);

    hook1 = new THREE.Mesh(new THREE.ConeGeometry(0.3, -1, 3), material3);
    hook1.position.set(x - 0.7, y - 6.25, z + 5);

    hook2 = new THREE.Mesh(new THREE.ConeGeometry(0.3, -1, 3), material3);
    hook2.position.set(x + 0.7, y - 6.25, z + 5);
    
    hook3 = new THREE.Mesh(new THREE.ConeGeometry(0.3, -1, 3), material3);
    hook3.position.set(x, y - 6.25, z + 5.7);

    hook4 = new THREE.Mesh(new THREE.ConeGeometry(0.3, -1, 3), material3);
    hook4.position.set(x, y - 6.25, z + 4.3);

    // const colliderGeo = new THREE.BoxGeometry(3, 2, 3);
    // const colliderMat = new THREE.MeshBasicMaterial({ color: 0x00ff00, transparent: true, opacity: 0.5 });
    // colliderGarra = new THREE.Mesh(colliderGeo, colliderMat);
    // colliderGarra.position.set(x, y - 7, z + 5);

    // Câmera móvel
    //mobileCamera = createMobileCamera();

    Garra = new THREE.Group();
    Garra.add(baseGarra);
    Garra.add(hook1);
    Garra.add(hook2);
    Garra.add(hook3);
    Garra.add(hook4);

    mobileCamera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 1000);
    mobileCamera.position.set(baseGarra.position.x, baseGarra.position.y + 0.5, baseGarra.position.z);
    mobileCamera.lookAt(baseGarra.position.x, baseGarra.position.y - 40, baseGarra.position.z);
    //var controls = new OrbitControls(mobileCamera, renderer.domElement);

    Garra.add(mobileCamera);    

    // colliderGarra = new THREE.Box3(new THREE. Vector3(), new THREE. Vector3());
    // colliderGarra.setFromObject(Garra);
    //Garra.add(colliderGarra)

    car.add(Garra);

    Garra.userData = {up: false, down: false, rotationClose: false, rotationOpen: false, raio: 1.5};
}

function addCarrinho(x, y, z) {
    'use strict';
    var base = new THREE.Mesh(new THREE.BoxGeometry(1, 0.5, 3), material3);
    base.position.set(x, y + 20, z + 5);

    var wheels1 = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 1, 20), material3);
    wheels1.position.set(x, y + 20.5, z + 4);
    
    var wheels2 = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 1, 20), material3);
    wheels2.position.set(x, y + 20.5, z + 6);
    
    var angle = Math.PI / 2; // 90º em radianos
    wheels1.rotation.z = angle;
    wheels2.rotation.z = angle;


    const carrinho = new THREE.Group();
    carrinho.add(base);
    carrinho.add(wheels1);
    carrinho.add(wheels2);

    carrinho.position.set(x, y - 14.5, z + 25);

    car.add(carrinho);
}

function addContentor(x, y, z) {
    'use strict';
    //purple
    material = new THREE.MeshBasicMaterial({ color: 0x800080, wireframe: true });
    materials.push(material);


    var parede1 = new THREE.Mesh(new THREE.BoxGeometry(10, 10, 0.3), material);
    parede1.position.set(x, y, z + 5);

    var parede2 = new THREE.Mesh(new THREE.BoxGeometry(10, 10, 0.3), material);
    parede2.position.set(x, y, z - 5);

    var parede3 = new THREE.Mesh(new THREE.BoxGeometry(0.3, 10, 10), material);
    parede3.position.set(x + 5, y, z);

    var parede4 = new THREE.Mesh(new THREE.BoxGeometry(0.3, 10, 10), material);
    parede4.position.set(x - 5, y, z);

    var base = new THREE.Mesh(new THREE.BoxGeometry(10, 0.3, 10), material);
    base.position.set(x, y - 5, z);

    Contentor = new THREE.Group();
    Contentor.add(parede1);
    Contentor.add(parede2);
    Contentor.add(parede3);
    Contentor.add(parede4);
    Contentor.add(base);

    Contentor.position.set(x, y + 5, z)
    scene.add(Contentor);
} 

function addObjetos(x, y, z) {
    'use strict';
    // orange
    material = new THREE.MeshBasicMaterial({ color: 0xffa000, wireframe: true });
    materials.push(material);

    objeto1 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), material);
    objeto1.position.set(x, y + 1, z + 15);
    objeto1.userData = {raio : 2/2};

    objeto2 = new THREE.Mesh(new THREE.DodecahedronGeometry(1.5, 0), material);
    objeto2.position.set(x - 9, y + 1, z - 16);
    objeto2.userData = {raio : 1.5};

    objeto3 = new THREE.Mesh(new THREE.IcosahedronGeometry(4, 0), material);
    objeto3.position.set(x - 13, y + 1, z + 2);
    objeto3.userData = {raio : 4}

    objeto4 = new THREE.Mesh(new THREE.TorusGeometry(2.5, 1.2, 8, 17), material);
    objeto4.position.set(x + 2, y + 2.3, z - 12);
    objeto4.userData = {raio : 2.5};

    objeto5 = new THREE.Mesh(new THREE.TorusKnotGeometry(2.2, 0.75, 22, 8), material);
    objeto5.position.set(x - 14, y + 1, z + 10);
    objeto5.userData = {raio : 2.2};

    objetos.push(objeto1, objeto2, objeto3, objeto4, objeto5);
    console.log(objetos);

    // const collider1 = new THREE.Box3(new THREE. Vector3(), new THREE. Vector3());
    // collider1.setFromObject(objeto1);

    // const collider2 = new THREE.Box3(new THREE. Vector3(), new THREE. Vector3());
    // collider2.setFromObject(objeto2);

    // const collider3 = new THREE.Box3(new THREE. Vector3(), new THREE. Vector3());
    // collider3.setFromObject(objeto3);
    // colliders.push(collider1, collider2, collider3);

    // const colliderGeo = new THREE.BoxGeometry(3, 3, 3);
    // const colliderMat = new THREE.MeshBasicMaterial({ color: 0x00fff0, transparent: true, opacity: 0.5 });
    // const collider1 = new THREE.Mesh(colliderGeo, colliderMat);
    // const collider2 = new THREE.Mesh(colliderGeo, colliderMat);
    // const collider3 = new THREE.Mesh(colliderGeo, colliderMat);

    // objeto1.add(collider1);
    // objeto2.add(collider2);
    // objeto3.add(collider3);
    //collider.position.set(x, y - 7, z + 5);

    scene.add(objeto1);
    scene.add(objeto2);
    scene.add(objeto3);
    scene.add(objeto4);
    scene.add(objeto5);
}

function createCrane(x, y, z) {
    'use strict';

    crane = new THREE.Object3D();

    // Objeto composto por rotator + cabine + porta lança + lança + contra-lança + contra-peso
    lanca = new THREE.Object3D();
    lanca.userData = {rotatingLanca: false, rotatingLancaNeg: false};

    // Objeto composto por carrinho + cabo + garra
    car = new THREE.Object3D();
    car.userData = {forward: false, backward: false};

    //red
    material = new THREE.MeshBasicMaterial({ color: 0xff0000, wireframe: true });
    //yellow
    material2 = new THREE.MeshBasicMaterial({ color: 0xffff00, wireframe: true });
    //blue
    material3 = new THREE.MeshBasicMaterial({ color: 0x0000ff, wireframe: true });
    materials.push(material, material2, material3);

    addBase(crane, 0, 0, 0);
    addTower(crane, 0, 12, 0);
    addRotator(lanca, 0, 22);
    addCabine(lanca, 0, 24, -1)
    addPortaLanca(lanca, 0, 29.5, 0);
    addLanca(lanca, 0, 25, 0);
    addContraLanca(lanca, 0, 25, 0);
    addTirantes(lanca, 0, 16, 0);
    addContraPeso(lanca, 0, 24, 0);
    addCarrinho(0, 10, -25);
    addCabos(car, 0, 17, -25);
    addGarra(0, 17, -25);
    //addContentor(20, 0, 0);

    crane.add(lanca);
    lanca.add(car);
    lanca.position.set(x, y + 0.5, z);

    scene.add(crane);

    crane.position.x = x;
    crane.position.y = y;
    crane.position.z = z;
}

function createScene() {
    'use strict';

    scene = new THREE.Scene();

    scene.add(new THREE.AxesHelper(10));

    createCrane(0, 0, 0);
    addObjetos(0, 0, 0);

    addContentor(10, 0, 0);
}

//////////////////////
/* CREATE CAMERA(S) */
//////////////////////

function createCameras() {
    'use strict';
    // Câmeras estáticas
    frontCamera = new THREE.OrthographicCamera(-50, 50, 50, -50, 1, 1000);
    frontCamera.position.set(0, 0, -100);
    frontCamera.lookAt(scene.position);
    
    sideCamera = new THREE.OrthographicCamera(
        // window.innerWidth / -2, // left
        // window.innerWidth / 2, // right
        // window.innerHeight / 2, // top
        // window.innerHeight / -2, // bottom
        -50, 50, 50, -50,
        1,
        1000
    );
    sideCamera.position.set(100, 0, 0);
    sideCamera.lookAt(scene.position);

    topCamera = new THREE.OrthographicCamera(-50, 50, 50, -50, 1, 1000); 
    topCamera.position.set(0, 100, 0);
    topCamera.lookAt(scene.position);

    sceneCamera1 = new THREE.OrthographicCamera(-50, 50, 50, -50, 1, 1000);
    sceneCamera1.position.set(50, 50, 50);
    sceneCamera1.lookAt(scene.position);

    sceneCamera2 = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 1000);
    sceneCamera2.position.set(50, 50, 50);
    sceneCamera2.lookAt(scene.position);

    // Adicionando as câmeras à cena
    scene.add(frontCamera);
    scene.add(sideCamera);
    scene.add(topCamera);
    scene.add(sceneCamera1);
    scene.add(sceneCamera2);
    //scene.add(mobileCamera);
    //baseGarra.add(mobileCamera);
}

/////////////////////
/* CREATE LIGHT(S) */
/////////////////////

////////////////////////
/* CREATE OBJECT3D(S) */
////////////////////////

//////////////////////
/* CHECK COLLISIONS */
//////////////////////

function checkCollisions(){
    'use strict';

    for (let i = 0; i < objetos.length; i++) {
        var object = objetos[i];
        var GarraPosi = new THREE.Vector3();
        
        baseGarra.getWorldPosition(GarraPosi);
        var distance = GarraPosi.distanceToSquared(object.position);

        // console.log("objeto:" + i + object.position.x, object.position.y, object.position.z);
        // console.log("garra:" + GarraPosi.x, GarraPosi.y, GarraPosi.z);
        // console.log("Distance: " + distance);

        if (distance <= (object.userData.raio + Garra.userData.raio)**2) {
            console.log("Collision detected with object " + i);
            handleCollisions(object);
            break;
        }
    }
}

///////////////////////
/* HANDLE COLLISIONS */
///////////////////////

function handleCollisions(objectCollided){
    'use strict';

    document.removeEventListener('keydown', onKeyDown);
    Garra.userData.rotationClose = true;

    

        setTimeout(function() {
            if (hook1.rotation.z >= 0.60){
                Garra.attach(objectCollided);
                Garra.userData.up = true;
                car.userData.forward = true;
            }
            setTimeout( function(){
                Garra.userData.up = true;
                car.userData.forward = true;
            }, 3000);
    
            setTimeout( function(){
                lanca.rotation.y = -Math.PI / 2;
            }, 3000);

            setTimeout( function(){
                car.userData.forward = false;
                Garra.userData.up = false;
                Garra.userData.down = true;

                setTimeout( function(){
                    Garra.remove(objectCollided);
                    Garra.userData.down = false;
                    Garra.userData.rotationClose = false;
                    Garra.userData.rotationOpen = true;
                    setTimeout( function(){
                        Garra.userData.rotationOpen = false;
                        document.addEventListener('keydown', onKeyDown);
                    }, 2000)
                }, 3000);
            }, 4000);
            
        }, 2500);
    }


////////////
/* UPDATE */
////////////

function update(){
    'use strict';

    var delta = clock.getDelta();

    if (lanca.userData.rotatingLanca) {
        lanca.rotation.y += 0.6 * delta;
    }

    if (lanca.userData.rotatingLancaNeg) {
        lanca.rotation.y -= 0.6 * delta;
    }
    
    if (car.userData.forward) {
        if (car.position.z > 0)
            car.position.z -= 5 * delta;
    }

    if (car.userData.backward) {
        if (car.position.z < 15)
            car.position.z += 5 * delta;
    }

    if (Garra.userData.up) {
        if (Garra.position.y < 12) {
            Garra.position.y += 0.2;
            cabos1.position.y += 0.1;
            cabos1.scale.y -= 0.014;
        }
    }

    if (Garra.userData.down) {
        if (Garra.position.y > -10) {
            Garra.position.y -= 0.2;
            cabos1.position.y -= 0.1;
            cabos1.scale.y += 0.014;
        }
    }

    if (Garra.userData.rotationClose) {
        if (hook1.rotation.z + hook2.rotation.z + hook3.rotation.x + hook4.rotation.x == 0 && hook1.rotation.z < 0.63) {
            hook1.rotation.z += 0.5 * delta;
            hook2.rotation.z -= 0.5 * delta;
            hook3.rotation.x += 0.5 * delta;
            hook4.rotation.x -= 0.5 * delta;
            // console.log("rotações dos hooks: 1 = " + hook1.rotation.z + "; 2 = " + hook2.rotation.z + "; 3 = " + hook3.rotation.x + "; 4 = " + hook4.rotation.x);
        }
    }

    if (Garra.userData.rotationOpen) {
        if (hook1.rotation.z + hook2.rotation.z + hook3.rotation.x + hook4.rotation.x == 0 && hook1.rotation.z > 0) {
            hook1.rotation.z -= 0.5 * delta;
            hook2.rotation.z += 0.5 * delta;
            hook3.rotation.x -= 0.5 * delta;
            hook4.rotation.x += 0.5 * delta;
            // console.log("rotações dos hooks: 1 = " + hook1.rotation.z + "; 2 = " + hook2.rotation.z + "; 3 = " + hook3.rotation.x + "; 4 = " + hook4.rotation.x);
        }
    }

}

/////////////
/* DISPLAY */
/////////////
function render() {
    'use strict';
    renderer.render(scene, activeCamera);
}

function ToggleWireframe() {
    'use strict';

    for (var i = 0; i < materials.length; i++) {
        materials[i].wireframe = !materials[i].wireframe;
    }
}

////////////////////////////////
/* INITIALIZE ANIMATION CYCLE */
////////////////////////////////
function init() {
    'use strict';

    // renderer init
    renderer = new THREE.WebGLRenderer({
        antialias: true
    });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0xbcd2e8, 1.0);
    document.body.appendChild(renderer.domElement);

    // Add cameras to your scene
    createScene();

    createCameras();
    activeCamera = sceneCamera1;
    //createCamera();

    clock = new THREE.Clock();

    //render();

    // Events
    window.addEventListener("resize", onResize);
    document.addEventListener('keydown', onKeyDown);
    document.addEventListener('keyup', onKeyUp);
}

/////////////////////
/* ANIMATION CYCLE */
/////////////////////
function animate() {
    'use strict';

    update();

    render();

    requestAnimationFrame(animate);
    

    if(movementBool)
        checkCollisions();
}

////////////////////////////
/* RESIZE WINDOW CALLBACK */
////////////////////////////

function onResize() {
    'use strict';

    renderer.setSize(window.innerWidth, window.innerHeight);

    if (window.innerHeight > 0 && window.innerWidth > 0) {
        activeCamera.aspect = window.innerWidth / window.innerHeight;
        activeCamera.updateProjectionMatrix();
    }
}

///////////////////////
/* KEY DOWN CALLBACK */
///////////////////////
function onKeyDown(event) {
    'use strict';

    /*‘1’ (frontal), ‘2’ (lateral), ‘3’ (topo), 
    ‘4’ (câmara fixa com projecção ortogonal), 
    ‘5’ (câmara fixa com projecção perspectiva) e 
    ‘6’ (câmara móvel com projecção perspectiva). */

    switch (event.keyCode) {
        case 49: // 1
            activeCamera = frontCamera;
            break;
        case 50: // 2
            activeCamera = sideCamera;
            break;
        case 51: // 3
            activeCamera = topCamera;
            break;
        case 52: // 4
            activeCamera = sceneCamera1;
            break;
        case 53: // 5
            activeCamera = sceneCamera2;    
            break;
        case 54: // 6
            activeCamera = mobileCamera;
            break;
        case 55: // 7
            ToggleWireframe();
            break;

        case 87: // W
            car.userData.forward = true;
            movementBool = true;
            break;
        case 83: // S
            car.userData.backward = true;
            movementBool = true;
            break;

        case 81: // Q
            lanca.userData.rotatingLanca = true;
            movementBool = true;
            break;
        
        case 65: // A
            lanca.userData.rotatingLancaNeg = true;
            movementBool = true;
            break;

        case 69: // E
            Garra.userData.up = true;
            movementBool = true;
            break;
        case 68: // D
            Garra.userData.down = true;
            movementBool = true;
            break;

        case 82: // R
            Garra.userData.rotationClose = true;
            movementBool = true;
            break;

        case 70: // F
            Garra.userData.rotationOpen = true;
            movementBool = true;
            break;

        default:
            break;
    }
}

///////////////////////
/* KEY UP CALLBACK */
///////////////////////

function onKeyUp(event){
    'use strict';

    switch (event.keyCode) {
        case 81: // Q
            lanca.userData.rotatingLanca = false;
            movementBool = false;
            break;
        case 65: // A
            lanca.userData.rotatingLancaNeg = false;
            movementBool = false;
            break;

            case 87: // W
            car.userData.forward = false;
            movementBool = false;
            break;
        case 83: // S
            car.userData.backward = false;
            movementBool = false;
            break;

        case 69: // E
            Garra.userData.up = false;
            movementBool = false;
            break;
            
        case 68: // D
            Garra.userData.down = false;
            movementBool = false;
            break;

        case 82: // R
            Garra.userData.rotationClose = false;
            movementBool = false;
            break;

        case 70: // F
            Garra.userData.rotationOpen = false;
            movementBool = false;
            break;

        default:
            break;
    }
}

init();
animate();