#!/usr/bin/node
// gives out a message depending on number of arguments passed

const arg = process.argv;
if (arg.length === 2) {
  console.log('No argument');
} else if (arg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
