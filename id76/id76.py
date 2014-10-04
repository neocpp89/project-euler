#!/usr/bin/env python
import sys

# turns out this is sequence A000065 (-1 + partitions of n)

def partition_function(n,known={}):
    if (n == 0):
        known[n] = 1
        return 1
    if (n < 0):
        return 0
    s = 0
    for k in range(1,n+1):
        leftn = n - (k*(3*k-1))/2
        rightn = n - (k*(3*k+1))/2
        if leftn in known:
            left = known[leftn]
        else:
            left = partition_function(leftn, known)
        if rightn in known:
            right = known[rightn]
        else:
            right = partition_function(rightn, known)
        s += ((-1)**(k+1) * (left + right))
    if n not in known:
        known[n] = s
    return s

def howtomake(n, known=None):
    if (known is not None and n in known):
        return known[n]

    s = set()
    for i in range(1, 1+n/2):
        tup = (i, n-i)
        f = howtomake(n-i, known)
        for t in f:
            s.add(tuple(sorted([i] + list(t))))
        s.add(tup)

    if (known is not None):
        known[n] = s

    return s

if (len(sys.argv) == 1):
    q = 100
else:
    q = int(sys.argv[1])

# m = howtomake(q, {})
# sums = map(lambda t: reduce(lambda x,y: x+y,t,0), list(m))
# bsums = [not (s == q) for s in sums]
# if any(bsums):
#    print 'Error in sum!'
# print len(m)

def numwaystomake(val, possible, known=None):
    if (val == 0):
        return 1
    if (val < 0 or (not possible and val > 0)):
        return 0
    s = numwaystomake(val, possible[:-1]) + numwaystomake(val - possible[-1], possible)
    return s 

# dont include 'q + 0'
print partition_function(q)-1
#print numwaystomake(q, range(1, q))
