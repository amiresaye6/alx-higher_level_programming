#!/usr/bin/node

const args = process.argv.slice(2);
const maxNum = parseInt(args[0]);

if (args.length > 0) {
  if (!isNaN(maxNum)) {
    for (let i = 0; i < maxNum; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
