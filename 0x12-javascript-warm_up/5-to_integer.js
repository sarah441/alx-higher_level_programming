#!/usr/bin/node
const newn = parseInt(process.argv[2]);
if (isNaN(newn))
{
	console.log('Not a number');
} 
else
{
	console.log('My number: ' + (newn));
}
