#!/usr/bin/env python

import sys

index=int(sys.argv[1])
for line in sys.stdin:
	fields = line.split(",")
	print "LongValueSum:" + fields[index] + "\t" + "1"
	
	