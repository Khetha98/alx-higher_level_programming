#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { 
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      if (i < this.height) { process.stdout.write('\n'); }
    }
  }

  rotate () {
    const temporaryHeight = this.height;
    this.height = this.width;
    this.width = temporaryHeight;
  }

  double () {
    [this.width, this.height] = [this.width, this.height]
      .map(prop => prop * 2);
  }
};
