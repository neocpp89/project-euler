#!/usr/bin/env python
import math
lim = 10 ** 6
leftof = 3.0 / 7.0

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


best = 0
bn = 0
bd = 0

for d in xrange(lim, lim-100, -1):
    n = int(d * leftof)
    pfd = prime_factors(d)
    pfn = prime_factors(n)
    while (len(set(pfd) & set(pfn)) != 0):
        n -= 1
        if (n == 0):
            break
        pfn = prime_factors(n)
    f =float(n) / float(d)
    if (f > best):
        best = f
        bn = n
        bd = d
        print f, n, d, pfn, pfd
