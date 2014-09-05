#!/usr/bin/env python
import datetime

c = 0
for yy in xrange(1901,2001):
    for mm in xrange(1,13):
        d = datetime.date(yy,mm,1)
        if d.weekday() == 6:
            c += 1
            print d
    
print c