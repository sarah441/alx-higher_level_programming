#!/usr/bin/node

const Sarasquare = require('./5-square');
module.exports = class Square extends Sarasquare
{
	charPrint (c)
	{
		const myChar = c === undefined ? 'X' : c;
		for (let i = 0; i < this.height; i++)
		{
			let myart = '';
			let y = 0;
			while (y < this.width)
			{
				myart += myChar;
				y++;
			}

			console.log(myart);
		}
	}
};
