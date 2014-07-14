#!/usr/bin/python
# -*- coding: utf-8 -*-

from pandocfilters import toJSONFilter

def process(key, value, format, meta):

	# find images and change their src paths to relative ones
	if key == 'Image':
		src = value[1][0]
		value[1][0] = '../images/' + src.split('/')[-1]

	# find links to old uploads and change their href paths to relative ones
	if key == 'Link':
		href = value[1][0]
		if 'programminghistorian.org/wp-content/uploads/' in href:
			value[1][0] = '../images/' + href.split('/')[-1]
		if 'programminghistorian.org/lessons/' in href:
		    value[1][0] = '../lessons/' + href.split('/')[-1]

if __name__ == "__main__":
	toJSONFilter(process)
