#!/usr/bin/node
let n = process.argv[2];

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let y = 0;
    let ex = '';

    while (y < n) {
      ex = ex + 'X';
      y++;
    }
    console.log(ex);
  }
}
