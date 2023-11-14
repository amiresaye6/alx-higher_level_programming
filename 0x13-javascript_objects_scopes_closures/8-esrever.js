#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const len = list.length();
  for (let i = 0; i < len; list++) {
    newList[len - i - 1] = list[i];
  }
  return (newList);
};
