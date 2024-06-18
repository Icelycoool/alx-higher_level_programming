#!/usr/bin/node

const args = process.argv;
const firstArg = args[2];

if (!isNaN(Number(firstArg))) {
  console.log('My number: ' + Number(firstArg));
} else {
  console.log('Not a number');
}
