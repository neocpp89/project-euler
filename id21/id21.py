#!/usr/bin/env python
import math

def aliquot(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    for i in xrange(1,lim+1):
        if n % i == 0:
            s += i + n/i
            
    return (s - n)

A063990_ambicable = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
# print sum(A063990_ambicable)

alist = []
for x in xrange(1,10001):
    alist.append(aliquot(x))
    
s = 0
for a in xrange(0, len(alist)):
    if (alist[a] == (a+1)):
        continue
    if (alist[a] < len(alist)):
        if (alist[alist[a] - 1] == (a+1)):
            s += (a + 1)
        
print s