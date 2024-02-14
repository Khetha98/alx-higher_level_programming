#!/usr/bin/node
// It a script that imports an array.
const data = require('./100-data');

const original = data.list;
const newList = original.map((value, index) => value * index);

console.log(original);
console.log(newList);
