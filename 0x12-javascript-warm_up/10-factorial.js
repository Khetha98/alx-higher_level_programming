#!/usr/bin/node
// Calculate and prints the factorial recursively
function factorial (n) {
    if (n === 1) {
      return (1);
    }
    return (n * factorial(n - 1));
  }
  const arg = process.argv;
  
  if (isNaN(arg[2])) {
    console.log('1');
  } else {
    let num = factorial(parseInt(arg[2], 10));
    console.log(num);
  }
