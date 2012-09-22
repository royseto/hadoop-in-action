#!/usr/bin/env python

import re, time

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts))

line = '177.23.21.50 - - [15/Sep/2012:00:07:45] "GET /flower_store/product.screen?product_id=FL-DSH-01 HTTP/1.1" 200 10901 "http://mystore.splunk.com/flower_store/category.screen?category_id=PLANTS&JSESSIONID=SD7SL1FF9ADFF2" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.10) Gecko/20070223 CentOS/1.5.0.10-0.1.el4.centos Firefox/1.5.0.10" 1604 1667'
m = pattern.match(line)
res = m.groupdict()

print res["time"]
tt = time.strptime(res["time"], "%d/%b/%Y:%H:%M:%S")
print tt[0] 
print tt[1]
print tt[2]
print tt[3]
t2 = (tt[0], tt[1], tt[2], tt[3], 0, 0, tt[6], tt[7], tt[8])
print t2
print time.asctime(t2)

fname = '/Users/royseto/src/hia/data/logfiles/apache1.splunk.com/access_combined.log'
with open(fname, 'r') as f:
	for x in f:
		print x.rstrip()
		


