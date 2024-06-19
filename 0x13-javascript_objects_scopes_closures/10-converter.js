#!/usr/bin/node

exports.converter = function (base) {
  return function (decimal) {
    return (decimal >>> 0).toString(base);
  };
};
