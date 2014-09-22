#!/usr/bin/env python
lim = 50 * 10 ** 6
plim = 10 ** 4

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

primes = filter(isprime, range(0, 1+plim))

psq = filter(lambda y: y <= lim, map(lambda x: x ** 2, primes))
pcu = filter(lambda y: y <= lim, map(lambda x: x ** 3, primes))
pfo = filter(lambda y: y <= lim, map(lambda x: x ** 4, primes))

s = set()

for a in psq:
    for b in pcu:
        for c in pfo:
            if (a+b+c < lim):
                s.add(a+b+c)

print len(s)
