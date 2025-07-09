#!/usr/bin/node

const { argv } = require('node:process');

for (let count = 2; count <= argv.length - 1; count++) {
  console.log(argv[count]);
}
