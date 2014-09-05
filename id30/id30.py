#!/usr/bin/env python
import math

def digit_power_sum(n, p):
    return sum([int(x) ** p for x in str(n)])

s = 0
for i in xrange(2,1000000):
    if i == digit_power_sum(i, 5):
        s += i
        print i
        
print 'total:', s