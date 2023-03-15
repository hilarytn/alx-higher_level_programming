#!/usr/bin/node

const process = require('process');
let arg = process.argv[2];
let temp = 1;

function factorial () {
  if (isNaN(arg)|| arg === 0) { console.log(1); } else {
    temp = temp * arg;
    arg--;
    if (arg > 1) { factorial(Number(arg)); } else { console.log(temp); }
    return 0;
  }
}

factorial(Number(arg));
