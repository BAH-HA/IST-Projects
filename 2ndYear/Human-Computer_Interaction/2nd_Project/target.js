// Target class (position and width)
class Target
{
  constructor(x, y, w, l, id)
  {
    this.x      = x;
    this.y      = y;
    this.width  = w;
    this.label  = l;
    this.id     = id;
    this.hit   = false;
  }
  
  // Checks if a mouse click took place
  // within the target
  clicked(mouse_x, mouse_y)
  {
    return dist(this.x, this.y, mouse_x, mouse_y) < this.width / 2;
  }

  // Draws the target (i.e., a circle)
  // and its label
  draw()
  {
    let fillColor, textColor;
    // Draw target
    if (this.hit) { // black target when hit
      fillColor = color(0,0,0);
    } 
    else {
      switch (this.label[0]) {
        case "A":
          fillColor = color(34,139,34);
          break;
        case "B":
          fillColor = color(170, 51, 106);
          break;
        case "C":
          fillColor = color(100,100,100);
          break;
        case "D":
          fillColor = color(127,0,255);
          break;
        case "E":
          fillColor = color(0,0,255);
          break;
        case "F":
          fillColor = color(0,0,139);
          break;
        case "G":
          fillColor = color(212, 175, 55);
          break;
        case "H":
          fillColor = color(0,255,127);
          break;
        case "I":
          fillColor = color(0,255,0);
          break;
        case "J":
          fillColor = color(127,255,0);
          break;
        case "K":
          fillColor = color(127,255,0);
          break;
        case "L":
          fillColor = color(255,255,0);
          break;
        case "M":
          fillColor = color(0,127,255);
          break;
        case "N":
          fillColor = color(165,0,82);
          break;
        case "O":
          fillColor = color(255,127,0);
          break;
        case "P":
          fillColor = color(255, 127.5, 255.0);
          break;
        case "Q":
          fillColor = color(0,0,255);
          break;
        case "R":
          fillColor = color(148,26,28);
          break;
        case "S":
          fillColor = color(255,255,255);
          break;
        case "T":
          fillColor = color(0,255,127);
          break;
        case "U":
          fillColor = color(0,255,0);
          break;
        case "V":
          fillColor = color(127,0,255);
          break;
        case "W":
          fillColor = color(60, 118, 70);
          break;
        case "X":
          fillColor = color(255,127,0);
          break;
        case "Y":
          fillColor = color(255,255,0);
          break;
        case "Z":
          fillColor = color(255,0,127);
          break;
        default:
          fillColor = color(255,255,255);
          
        }
    }
    // Choose text color based on contrast
    let y = 0.299 * red(fillColor) + 0.587 * green(fillColor) + 0.114 * blue(fillColor);
    textColor = y > 128 ? color(0) : color(255);
    
    fill(fillColor);
    circle(this.x, this.y, this.width);
    
    // Draw label
    textFont("Arial", 16);
    textAlign(CENTER, CENTER);
    fill(textColor);
    text(this.label, this.x, this.y);
    textFont("Arial", 26);
    textAlign(CENTER, TOP);
    fill(textColor);
    text(this.label.slice(0,2), this.x, this.y-33);
    }
}
