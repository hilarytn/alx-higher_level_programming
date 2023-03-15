#!/usr/bin/node

const process = require('process');
let arg = process.argv;

if (!arg[2] || arg.length === 3)
        console.log(0);
else {
        let arr = [];
        let p = 0;
        for (let j = 2; j < arg.length; j++) {
                arr[p] = parseInt(arg[j])
                p++;
        }
        arr.sort();
        console.log(arr[arr.length - 2]);
}

