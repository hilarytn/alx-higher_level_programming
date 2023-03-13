#!/usr/bin/node

const process = require('process')

if (process.argv[2] === undefined) 
  console.log('Not a number');
else if (typeof(process.argv[2]) === 'string'){
  if ((parseInt(process.argv[2])))
    console.log(`My number: ${parseInt(process.argv[2])}`);
  else
    console.log('Not a number');
}
else
  console.log(`My number: ${parseInt(process.argv[2])}`);
