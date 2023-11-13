#!/usr/bin/env node

const args = process.argv.slice(2);
let number = parseInt(args[0]);
let res = 1;

if (!isNaN(number)) {
  while (number > 0) {
    res *= number;
    number--;
  }
  console.log(res);
} else {
  console.log(1);
}
