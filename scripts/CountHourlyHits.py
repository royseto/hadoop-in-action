#!/usr/bin/env python

import re, time

log_format = [
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
pattern = re.compile(r'\s+'.join(log_format))
fname = '/Users/royseto/src/hia/data/logfiles/apache1.splunk.com/access_combined.log'

with open(fname, 'r') as f:
    for line in f:
        m = pattern.match(line)
        res = m.groupdict()
        tt = time.strptime(res["time"], "%d/%b/%Y:%H:%M:%S")
        t2 = (tt[0], tt[1], tt[2], tt[3], 0, 0, tt[6], tt[7], tt[8])
        print "LongValueSum:" + time.asctime(t2) + "\t1"

