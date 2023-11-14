#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocurances = 0;
  let i = 0;
  if (list !== undefined && searchElement !== undefined) {
    while (list[i] !== undefined) {
      if (list[i] === searchElement) {
        ocurances++;
      }
      i++;
    }
  }
  return (ocurances);
};
