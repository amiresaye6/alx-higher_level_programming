#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv.slice(2);
const firstNumber = parseInt(args[0]);
const secondNumber = parseInt(args[1]);

if (!isNaN(firstNumber) && !isNaN(secondNumber)) {
  console.log(add(firstNumber, secondNumber));
} else {
  console.log('NaN');
}
