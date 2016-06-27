#!/usr/bin/env python
import math
from bisect import bisect_left, bisect_right
lim = 150 * 10 ** 6
# lim = 1 * 10 ** 6

def prime_sieve(upto):
    sieve = [True]*(upto)
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2, upto):
        if (sieve[i]):
            for j in xrange(i * i, upto, i):
                sieve[j] = False
    return [i for i,p in enumerate(sieve) if p]

from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def isprime(n):
    if (n == 0 or n == 1):
        return False
    if (n == 2):
        return True
    if (n == 3):
        return True

    if (n % 6 != 1 and n % 6 != 5):
        return False
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

# primes = prime_sieve(lim)
# sieve_size = 100000
# primes = prime_sieve(sieve_size)
# print 'Done generating primes.'

# x = [xx*xx for xx in x]
# x = [(xx*xx + 1) for xx in x]
# x = filter(lambda nn: nn % 6 == 0 or nn % 6 == 4, x)
# x = [xx+1 for xx in x]
# for p in primes:
#    x = filter(lambda nnpo: nnpo % p != 0, x)
# print 'Done pre-filtering.'
x = filter(lambda n: all([probably_prime(n*n + z, 10) for z in [1,3,7,9,13,27]]) , range(1, lim+1))
# x = filter(lambda n: probably_prime(n*n + 1, 10), x)
# x = filter(lambda n: probably_prime(n*n + 3, 10), x)
# x = filter(lambda n: probably_prime(n*n + 7, 10), x)
# x = filter(lambda n: probably_prime(n*n + 9, 10), x)
# x = filter(lambda n: probably_prime(n*n + 13, 10), x)
# x = filter(lambda n: probably_prime(n*n + 27, 10), x)
# x = filter(lambda nnpo: probably_prime(nnpo, 10), x)
# x = filter(lambda n: isprime(n*n + 1), x)
# x = filter(lambda n: isprime(n*n + 3), x)
# x = filter(lambda n: isprime(n*n + 7), x)
# x = filter(lambda n: isprime(n*n + 9), x)
# x = filter(lambda n: isprime(n*n + 13), x)
# x = filter(lambda n: isprime(n*n + 27), x)

def verify(n):
    f = False
    t = True
    want = [
        t, f, t, f, f,
        f, t, f, t, f,
        f, f, t, f, f,
        f, f, f, f, f,
        f, f, f, f, f,
        f, t]
    v = t
    for c in range(0, len(want)):
       v &= isprime(n*n + c + 1) == want[c]
    return v

x = filter(verify, x)
print x
print sum(x)
