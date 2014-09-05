#!/usr/bin/env python
import math

def pow_mod(a,b,n):
    m = 1
    for i in xrange(0,b):
        m = m*a % n
        if (m == 0):
            break
        
    return m

s = 0
for i in xrange(1,1001):
    s += pow_mod(i,i,1e10)
    s = s % 1e10
    print int(s)