#!/usr/bin/node

const f = require('fs');
const thefilename = process.argv[2];
const thecontent = process.argv[3];

f.writeFile(thefilename, thecontent, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
