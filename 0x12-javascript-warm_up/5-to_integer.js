#!/usr/bin/node
// prints a string based on if arg is a number

const arg = process.argv;
const number = parseInt(arg[2], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
