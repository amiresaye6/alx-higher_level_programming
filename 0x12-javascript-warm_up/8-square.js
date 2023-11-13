#!/usr/bin/node

const args = process.argv.slice(2);
const maxNum = parseInt(args[0]);

if (args.length > 0) {
  if (!isNaN(maxNum)) {
    let strX = '';
    for (let i = 0; i < maxNum; i++) {
      strX += 'X';
    }
    for (let j = 0; j < maxNum; j++) {
      console.log(strX);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
