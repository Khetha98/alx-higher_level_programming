#!/usr/bin/node

const therequest = require('request');
const f = require('fs');
const theurl = process.argv[2];
const thefile = process.argv[3];

therequest(theurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    f.writeFile(thefile, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
