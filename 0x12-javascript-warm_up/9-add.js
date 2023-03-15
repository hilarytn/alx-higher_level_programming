#!/usr/bin/node

const process = require('process');
const sum = parseInt(process.argv[2]) + parseInt(process.argv[3]);
console.log(sum);
