#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  const result = console.log(`${count}: ${item}`);
  count++;
  return result;
};
