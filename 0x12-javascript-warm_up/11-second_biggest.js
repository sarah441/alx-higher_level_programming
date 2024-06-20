#!/usr/bin/node

function f(a) {
  if (a.length === 0 || a.length === 1) 
	return console.log(0);
  const n = a.map(Number);
n.sort((a, b) => b - a);
return console.log(n[1] !== n[0] ? n[1] : 0);
}
const a = process.argv.slice(2);
f(a);
