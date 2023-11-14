#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log('hi there');
  }
}
module.exports = Rectangle;
const rec = new Rectangle(2, 2);
rec.print();
