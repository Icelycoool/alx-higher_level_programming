#!/usr/bin/node

const arg = Number(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 1 || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(arg));
