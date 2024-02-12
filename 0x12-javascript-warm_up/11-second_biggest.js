#!/usr/bin/node
// Checks second biggest integer in a list of arguments

const arg = process.argv;

if (isNaN(arg[2])) {
  console.log('0');

} else if (arg.length === 3) {
  console.log('0');
} else {
  let firstnum = parseInt(arg[2], 10);
  let secondnum = parseInt(arg[3], 10);
  for (let i = 2; i < arg.length; i++) {
    if (parseInt(arg[i], 10) > firstnum) {
      secondnum = firstnum;
      firstnum = parseInt(arg[i], 10);
    }
    if (parseInt(arg[i], 10) > secondnum && parseInt(arg[i], 10) < firstnum) {
      secondnum = parseInt(arg[i], 10);
    }
  }
  console.log(secondnum);
}
