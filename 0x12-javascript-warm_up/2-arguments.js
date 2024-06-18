#!/usr/bin/node
const args_numbers = process.argv.length;

if (args_numbers > 2) {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
