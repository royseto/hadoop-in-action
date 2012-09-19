#!/usr/bin/env python
# encoding: utf-8
"""
RandomSample.py

Created by Roy Seto on 2012-09-15.
"""

import sys, random

for line in sys.stdin:
	if (random.randint(1,100) <= int(sys.argv[1])):
		print line.strip()
		

