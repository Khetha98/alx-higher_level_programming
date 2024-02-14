#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if ((w >= 1) && (h >= 1)) {
        [this.width, this.height] = [w, h];
      }
    }
  
    print () {
      let size = this.height;
      while (size > 0) {
        console.log('X'.repeat(this.width));
        size -= 1;
      }
    }
  };
