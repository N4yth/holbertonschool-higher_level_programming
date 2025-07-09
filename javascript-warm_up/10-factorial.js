#!/usr/bin/node

const { argv } = require('node:process');

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
if (isNaN(argv[2])) {
  console.log(1);
} else {
  console.log(factorial(argv[2]));
}
