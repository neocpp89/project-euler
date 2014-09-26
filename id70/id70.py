#!/usr/bin/env python
import math
from bisect import bisect_left, bisect_right
lim = 10 ** 7

def prime_sieve(upto):
    sieve = [True]*(upto)
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2, upto):
        if (sieve[i]):
            for j in xrange(i * i, upto, i):
                sieve[j] = False
    return [i for i,p in enumerate(sieve) if p]

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

primes = prime_sieve(lim)
print 'Done generating primes.'

def pftotient(pl):
    pf = list(set(pl))
    n = reduce(lambda x, y: x*y, pl, 1)
    num = n * reduce(lambda x, y: x*(y-1), pf, 1)
    den = reduce(lambda x, y: x*y, pf, 1)
    return (num / den)

def totient_factor(p):
    return float(p) / float(p-1)

def is_totient_permuation(pl):
    n = reduce(lambda x, y: x*y, pl, 1)
    return (sorted(str(n)) == sorted(str(pftotient(pl))))

totients = map(totient_factor, primes)

gbest = max(primes)

def bandb(upper, lower, current, lim, plist, best=None, tc=None):
    global gbest
    if (tc is not None and tc >= gbest):
        return None        

    if current == [] or current is None:
        n = 1
        c = []
    else:
        n = reduce(lambda x,y: x*y, current, 1)
        c = current

    if (upper is None or lower is None):
        li = 0
        ui = len(plist)-1
    else:
        if (upper <= lower):
            return None
        
        li = bisect_left(plist, lower)
        ui = bisect_right(plist, upper)
        if (ui >= len(plist)):
            ui = len(plist) - 1

        if (ui <= li):
            return None

    i = ui
    if tc is None:
        tc = 1
    else:
        while (tc*totients[li] > gbest and li < i):
            li += 1

    while i >= li:
        while (n*plist[i] > lim and i >= li):
            i -= 1
        if (i < li):
            break
        cc = list(c)
        cc.append(plist[i])
        # print cc, tc, tc+totients[i], best
        # print cc
        if is_totient_permuation(cc):
            t = float(n*plist[i]) / float(pftotient(cc))
            if (t < gbest):
                gbest = t
                print n*plist[i], cc, t, gbest
                while (tc*totients[li] > gbest and li < i):
                    li += 1
            i -= 1
        else:
            i -= 1
        if (tc*totients[i] < gbest):
            bandb(lim / (n*plist[i]), 0, cc, lim, plist, gbest, tc*totients[i])

bandb(None, None, [], lim, primes)
