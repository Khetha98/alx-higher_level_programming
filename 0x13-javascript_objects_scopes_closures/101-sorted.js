#!/usr/bin/node
const data = require('./101-data');

const original = data.dict;
const newDict = {};

for (const userId in original) {
  const occurrence = original[userId];
  if (!newDict[occurrence]) {
    newDict[occurrence] = [userId];
  } else {
    newDict[occurrence].push(userId);
  }
}

console.log(newDict);
