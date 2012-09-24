#!/usr/bin/env python
# Copy stdin to stdout without modification

import sys

for line in sys.stdin:
	print line.rstrip()
	