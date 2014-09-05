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

def make_cycle(p, start):
    seen = set([])
    d = start
    c = 0
    while d not in seen:
        seen.add(d)
        d = d * 10 % p
        if d == 0:
            c = 0
            break
        c += 1
    
    return c
    
a = [aliquot(x) for x in xrange(0,1001)]
print a

prime = [x for x in xrange(0,len(a)) if a[x] == 1]
print prime

cycles = [make_cycle(p, 1) for p in prime]
print cycles
print max(cycles), prime[cycles.index(max(cycles))]

# recip = map(lambda p: 1.0/p, prime)
# print recip
