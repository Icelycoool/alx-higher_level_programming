#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c !== undefined && c !== null) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
