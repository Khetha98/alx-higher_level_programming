#!/usr/bin/node

const f = require('fs');
const thefilename = process.argv[2];

f.readFile(thefilename, 'utf-8', (error, content) => {
    if (error) {
      console.log(error);
    } else {
      console.log(content);
    }
});
