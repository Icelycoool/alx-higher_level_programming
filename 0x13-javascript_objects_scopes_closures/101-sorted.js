#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];

  if (newDict[occurrences]) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
});

console.log(newDict);
