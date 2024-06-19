#!/usr/bin/node
exports.nbOccurences = function (list, searchElement)
{
	let nOccurrences = 0;
	for (let s = 0; s < list.length; s++)
	{
		if (searchElement === list[s])
		{
			nOccurrences++;
		}
	}
	return nOccurrences;
};
