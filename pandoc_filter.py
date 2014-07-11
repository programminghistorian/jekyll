#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandocfilters import toJSONFilter

def process(key, value, format, meta):
	if key == 'Image':
		src = value[1][0]
		value[1][0] = '../images/' + src.split('/')[-1]
	if key == 'Link':
		href = value[1][0]
		if 'programminghistorian.org/wp-content/uploads/' in href:
			value[1][0] = '../images/' + href.split('/')[-1]

if __name__ == "__main__":
	toJSONFilter(process)
