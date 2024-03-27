#!/usr/bin/node

const request = require('request');
const theid = process.argv[2];
const theurl = 'https://swapi-api.hbtn.io/api/films/';
request.get(theurl + theid, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
