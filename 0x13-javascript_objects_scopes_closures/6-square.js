#!/usr/bin/node

const Square_old = require('./5-square');

class Square extends Square_old {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let sign;
    if (typeof (c) === undefined) {
      sign = c;
    } else {
      sign = 'X';
    }
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += sign;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }
}
module.exports = Square;
