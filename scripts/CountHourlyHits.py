#!/usr/bin/env python

import sys, re, time

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

for line in sys.stdin:
    m = pattern.match(line)
    res = m.groupdict()
    tt = time.strptime(res["time"], "%d/%b/%Y:%H:%M:%S")
    t2 = (tt[0], tt[1], tt[2], tt[3], 0, 0, tt[6], tt[7], tt[8])
    print "LongValueSum:" + time.asctime(t2) + "\t1"
