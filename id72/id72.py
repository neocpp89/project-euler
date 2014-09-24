#!/usr/bin/env python
import math
lim = 10 ** 6

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

def totient(n):
    pf = list(set(prime_factors(n)))

    num = n * reduce(lambda x, y: x*(y-1), pf, 1)
    den = reduce(lambda x, y: x*y, pf, 1)

    return (num / den)

c = 0
for d in xrange(2,1+lim):
    c += totient(d)
print c
