#!/usr/bin/env python
# freq.py
# by Adam Cotenoff (@acotenoff)
# 23 October 2013
import sys, re, operator

def main():
	BAR = u'\u2588' # unicode for printed bar
	d = {} # initialize empty dict

	# Usage checking
	if len(sys.argv) != 2: 
		print 'Figure it out! - Usage: freq.py [wordlist]'
		return -1

	# Opens file, reads from file, converts to lowercase, and removes apostrophe's
	text = open(sys.argv[1], 'r').read().lower().translate(None, '\'')
	text = re.sub('[^0-9a-zA-Z]+', ' ', text).split() # replaces all non-alpha numeric characters
	
	# Add string to dict and increment value if it is seen
	for i in range(0, len(text)):
		if text[i] in d:
			d[text[i]] += 1
		else:
			d[text[i]] = 1

	d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True) # sorts dict items from max to min

	max_count = float(d[0][1]) # the most times a word appears
	# create a list with only the values of the dict
	values = []
	for i in range(0, len(d)):
		values.append(d[i][0])
	
	max_length = len(max(values, key=len)) + 1
	# prints and aligns results
	for i in range(0, len(values)):
		temp = values[i] + ":"
		print temp.rjust(max_length, ' ') + int(((d[i][1] / max_count) * 100)) * BAR # normalizes data

if __name__ == "__main__":
	main()
