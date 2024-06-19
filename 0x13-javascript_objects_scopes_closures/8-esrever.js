#!/usr/bin/node
exports.esrever = function (list)
{
	let len = list.length - 1;
	let i = 0;
	{
		for (let i = 0; i < len/ 2; i++)
		{
			const spac = list[i];
			list[i] = list[list.length - 1 - i];
			list[list.length - 1 - i] = spac;
		}
	}
	return list;
};
