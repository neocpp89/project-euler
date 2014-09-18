#!/usr/bin/python
import math
import sys

sys.setrecursionlimit(15000)

def num_ways_to_make(want, possible):
    if (want == 0):
        return 1
    if (want <= 0 or not possible):
        return 0
    return num_ways_to_make(want, possible[:-1]) + num_ways_to_make(want-possible[-1], possible)

def is_prime(n):
    if (n == 0 or n == 1):
        return False
    lim = int(math.sqrt(n))+1
    for x in range(2,lim):
        if (n % x == 0): 
            return False
    return True

lim = 10 ** 5

primes = set(x for x in range(0, lim+1) if is_prime(x))
composites = set(range(0, lim+1)) - primes

lp = list(primes)

for n in range(0, lim+1):
    if num_ways_to_make(n, filter(lambda x: x <= n, lp)) > 5000:
        print n, num_ways_to_make(n, filter(lambda x: x <= n, lp))
        break
