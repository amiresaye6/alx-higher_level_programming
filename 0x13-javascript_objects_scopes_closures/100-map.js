#!/usr/bin/node

const list = require('./100-data.js');
let index = 0;
const newList = list.map((x) => {
  x *= index;
  index++;
});
console.log(list);
console.log(newList);
