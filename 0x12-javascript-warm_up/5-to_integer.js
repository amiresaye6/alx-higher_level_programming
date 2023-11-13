#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length > 0) {
  const number = parseInt(args[0]);
  if (!isNaN(number)) {
    console.log('My number: ' + number);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
