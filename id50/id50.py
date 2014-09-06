#!/usr/bin/env python
import math

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

def printf(x):
    print x

maxsearch = 1000000

try:
    with open('primes.txt') as f:
        primes = map(int, f)
    print primes[0], primes[-1]
except:
    primes = [x for x in range(0,maxsearch+1) if isprime(x)]
    map(printf, primes)

primes = filter(lambda p: p < maxsearch, primes)

def findit(plist, m):
    ijdiff = len(plist)-1
    si = sum(plist)
    # filter out sequences where the smallest sum is too large
    while (si > m):
        si = si - plist[ijdiff]
        ijdiff -= 1
    si += plist[ijdiff]
    while True:
        si = si - plist[ijdiff]
        s = si
        for i in range(0,len(plist)-ijdiff):
            j = i + ijdiff
            # print i,j
            s = s + plist[j] - plist[i]
            if (s < m):
                if (s in plist):
                    print i,j,s
                    return s
        ijdiff -= 1
        print ijdiff
    return None

findit(primes, maxsearch)

