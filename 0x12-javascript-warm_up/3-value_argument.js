#!/usr/bin/node
// it prints the first argument passed to it

const arg = process.argv;
if (arg[2] === undefined) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
