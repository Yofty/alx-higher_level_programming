#!/usr/bin/node
const num = math.floor(Number(process.argv[2]));
console.log(isNaN(num) ?'Not a number' : 'my number: ${num}');
