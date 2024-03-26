#!/usr/bin/node

const therequest = require('request');
const themovieId = process.argv[2];
const theurl = `https://swapi-api.alx-tools.com/api/films/${themovieId}`;

therequest.get(theurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
