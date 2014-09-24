#!/usr/bin/env python
import math
lim = 12000
leftof = 1.0 / 2.0
rightof = 1.0 / 3.0

def prime_factors(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    pf = []
    for i in xrange(2,lim+1):
        while n % i == 0:
            pf.append(i)
            n = n / i
    if n != 1:
        pf.append(n)
    return pf

c = 0

for d in xrange(4,1+lim):
    n = int(d * leftof)
    pfd = prime_factors(d)
    pfn = prime_factors(n)
    while ((float(n) / float(d)) > rightof):
        if (len(set(pfd) & set(pfn)) == 0):
            c += 1
        n -= 1
        if (n <= 0):
            break
        pfn = prime_factors(n)

print c
