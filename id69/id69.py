#!/usr/bin/env python
import math
lim = 10 ** 6

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

# primes = filter(isprime, range(0, 1+lim))

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

    r = n
    for p in pf:
        r *= (1.0 - (1.0/p))

    return r

t = map(lambda x: float(x)/totient(x), range(2, 1+lim))
print (2+t.index(max(t)))
