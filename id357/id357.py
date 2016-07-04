#!/usr/bin/env python
import math
from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

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

def divsiors(n):
    s = int(math.sqrt(n))
    d = []
    for i in range(1, s+1):
        if n % i == 0:
            d.append(i)
            d.append(n / i)
    return d

def need_to_check(n):
    s = int(math.sqrt(n))
    d = []
    for i in range(1, s+1):
        if n % i == 0:
            d.append(i + (n / i))
    return d

def check_all_sum_divisors_prime(n, k = 100):
    s = int(math.sqrt(n))
    d = []
    for i in range(1, s+1):
        if n % i == 0:
            if not probably_prime(i + (n / i), k):
                return False
    return True

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

upto = 100000000

s = 0
for i in range(1, upto + 1):
    if not probably_prime(i + 1, 10):
        continue
    if not probably_prime(2 + i / 2, 10):
        continue
    print i
    # l = need_to_check(i)
    # if all(map(lambda p: probably_prime(p, 100), l)):
    if check_all_sum_divisors_prime(i):
        s += i
print s
