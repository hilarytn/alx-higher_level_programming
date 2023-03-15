#!/usr/bin/node

const process = require('process');

if (parseInt(process.argv[2])) {
  let str = '';
  for (let i = 1; i <= process.argv[2]; i++) {
    str += 'x';
  }
  for (let j = 1; j <= process.argv[2]; j++) {
    console.log(str);
  }
} else { console.log('Missing size'); }
