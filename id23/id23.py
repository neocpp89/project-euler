#!/usr/bin/env python
import math

def aliquot(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    for i in xrange(1,lim+1):
        if n % i == 0:
            if (i == n/i):
                s += i
            else:
                s += i + n/i
            
    return (s - n)

A063990_ambicable = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
# print sum(A063990_ambicable)

alist = []
for x in xrange(1,28124):
    alist.append(aliquot(x))
# print alist
    
abundant = [] 
for a in xrange(0, len(alist)):
    if (alist[a] > (a+1)):
        abundant.append(a+1)
# print abundant

abundant_set = set([])
for elem in abundant:
    abundant_set = abundant_set | set([(x + elem) for x in abundant])

# print abundant_set
    
wholeset = set(range(1,28124))

nona = (wholeset - abundant_set)

print nona

print sum([x for x in nona])
