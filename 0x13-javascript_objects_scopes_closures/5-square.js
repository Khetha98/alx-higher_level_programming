#!/usr/bin/node

const Rectangle = require('./4-rectangle');

//It square class 
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
