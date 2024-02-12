#!/usr/bin/node
// Prints out 'C is fun'

const arg = process.argv;

const number = parseInt(arg[2], 10);
if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < arg[2]; i++) {
    console.log('C is fun');
  }
}
