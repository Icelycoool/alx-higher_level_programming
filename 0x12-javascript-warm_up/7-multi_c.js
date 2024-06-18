#!/usr/bin/node

const num = process.argv[2];

if (!isNaN(Number(num))) {
  for (let i = 0; i < Number(num); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
