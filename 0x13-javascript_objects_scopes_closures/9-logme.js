#!/usr/bin/node
let numbersarg = 0;


exports.logMe = function (item) {
  console.log(numbersarg + ': ' + item);
  numbersarg++;
};
