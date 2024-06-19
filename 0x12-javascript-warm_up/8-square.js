#!/usr/bin/node

const args = process.argv[2];

if (!isNaN(Number(args))) {
  const size = Number(args);
  for (let i = 0; i < Number(args); i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
