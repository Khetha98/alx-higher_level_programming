#!/usr/bin/node
// Prints addition of 2 numbers
function add (a, b) {
    return a + b;
  }
  const arg = process.argv;
  const number1 = parseInt(arg[2], 10);
  const number2 = parseInt(arg[3], 10);
  console.log(add(number1, number2));
