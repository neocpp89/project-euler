#!/usr/bin/env python
from itertools import combinations
from math import log

lim = 100

def isprime(n):
    if (n == 0 or n == 1):
        return False
    if (n == 2):
        return True
    d = 2
    while d*d <= n:
        if (n % d) == 0:
            return False
        d += 1
    return True

primes = filter(isprime, range(0,1+lim))
logprimes = map(log, primes)
print primes
print logprimes

ulim = 10 ** 9
logulim = log(ulim)

def num_hamming(llp, lu):
    if (lu < 0):
        return 0
    if (len(llp) == 0):
        return 1
    c = 0
    c += num_hamming(llp, lu-llp[-1]) + num_hamming(llp[:-1], lu)
    return c

print num_hamming(logprimes, logulim)
