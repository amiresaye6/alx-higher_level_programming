#!/usr/bin/node

let itra = 0;
exports.logMe = function (item) {
  console.log(itra + ': ' + item);
  itra++;
};
