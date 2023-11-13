#!/usr/bin/node
if (process.argv.length === 2) {
    console.log(0);
} else if (process.argv.length === 3) {
    console.log(0);
} else {
    let maxNumber = Number(process.argv[2]);
    for (let i = 3; i < process.argv.length; i++) {
        if (Number(process.argv[i]) > maxNumber) {
            maxNumber = Number(process.argv[i]);
        }
    }
    let secondMaxNumber = Number(process.argv[2])
    for (let i = 3; i < process.argv.length; i++) {
        if (Number(process.argv[2]) > secondMaxNumber && Number(process.argv[2]) < maxNumber) {
            secondMaxNumber = Number(process.argv[2]);
        }
    }
    console.log(secondMaxNumber);
}
