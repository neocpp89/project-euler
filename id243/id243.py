#!/usr/bin/env python
import math
# we know that if n1 = prod(primes(2 to 21)), totient(n1)/n1 > 15499/94744
# but for n2 = prod(primes(2 to 23), totient(n2)/n2 < 15499/94744
# from the totient maximum problem (id69), we know the least resilient numbers
# have the form of n1 and n2.
start = 2*3*5*7*11*13*17*19*23
# since we actually want totient(n)/(n-1), we can search for multiples of n2
# to see when it becomes less than the target. if we get to 29, we are at the
# next least-resilient number and probably need to rethink this
mullim = 29

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

def resilience(n):
    return float(totient(n)) / (n-1)

target = 15499.0 / 94744.0
for d in xrange(1,1+mullim):
    if resilience(d*start) < target:
        print d*start
        break

