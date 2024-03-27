#!/usr/bin/node

const f = require('fs');
const thefile = process.argv[2];

f.readFile(thefile, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
