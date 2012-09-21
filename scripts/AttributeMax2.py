#!/usr/bin/env python

import sys

index = int(sys.argv[1])
max = 0
max_line = ""

for line in sys.stdin:
	fields = line.strip().split(",")
	if fields[index].isdigit():
		val = int(fields[index])
		if (val > max):
			max = val	
			max_line = line
else:	
	print max_line.rstrip()
			