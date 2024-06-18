#!/usr/bin/node
const ar = process.argv[2];

if (!parseInt(ar))
{
  console.log('Missing number of occurrences');
} 
else 
{
  for (let u = 0; u < ar; u++) 
	{
    console.log('C is fun');
  }
}
