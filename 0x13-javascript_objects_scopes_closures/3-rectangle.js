#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const sign = 'X';
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += sign;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}
module.exports = Rectangle;
