#!/usr/bin/node
const therequest = require('request');
const theurl = process.argv[2];

therequest.get(theurl, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
