#!/usr/bin/node

const therequest = require('request');
const theurl = process.argv[2];
const thecharacterId = '18';
let c = 0;

therequest.get(theurl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(thecharacterId)) {
          c += 1;
        }
      });
    });
    console.log(c);
  }
});
