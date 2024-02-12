#!/usr/bin/node
// Prnts the square of given size
const arg = process.argv;
const s = parseInt(arg[2], 10);
const r = [];
if (isNaN(s)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < s; i++) {
    r.push('X');
  }
  for (let i = 0; i < s; i++) {
    console.log(r.join(''));
  }
}
