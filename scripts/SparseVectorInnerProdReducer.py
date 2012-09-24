#!/usr/bin/env python

import sys

(last_key, last_val, rsum) = (None, 0.0, 0.0)

for line in sys.stdin:
	(key, txt_val) = line.split("\t")
	val = float(txt_val)
	
	if last_key and last_key == key:
 		rsum += last_val * val
		
	(last_key, last_val) = (key, val)
	
print last_key + "\t" + str(rsum)

