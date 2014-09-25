#!/usr/bin/env python
import math
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

primes = prime_sieve(lim)[::-1] #start with largest primes first
print 'Done generating primes.'
#for d in xrange(1+lim, 2, -1):
#m = 1000
#for d in range(2, 1+lim):
#    c = totient(d)
#    if (tuple(sorted(str(c))) == tuple(sorted(str(d)))):
#        if (float(d) / float(c) < m):
#            m = float(d) / float (c)
#            print c, d, m

def test(n):
    if (len(n) == 0):
        return False
    prod = reduce(lambda x,y: x*y, n, 1)
    print n
    if (prod > lim):
        return False
    pf = list(set(n))
    t = (prod * reduce(lambda x, y: x*(y-1), pf, 1)) / reduce(lambda x, y: x*y, pf, 1)
    f = tuple(sorted(str(prod))) == tuple(sorted(str(t)))
    if f:
        print prod, t
    return f

def test_number(maxdepth, func, plist, depth=1, current=[]):
    if (depth > maxdepth or plist == []):
        return False
    
    #if func(current):
    #    return True

    if (current != []):
        partial_prod = reduce(lambda x,y: x*y, current, 1)
        i = 1
        p = plist[-i]
        while p*partial_prod < lim:
            p = plist[-i]
            i += 1
    else:
        i = 0
    for n in plist[-i:]:
        c = list(current)
        c.append(n)
        if (func(c) or test_number(maxdepth, func, plist, depth+1, c)):
            return True
    
    return False

for d in range(1,4):
    # fp = filter(lambda p: p ** d < lim, primes)
    if (test_number(d, test, primes)):
        break
