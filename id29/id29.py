#!/usr/bin/env python
import math

def aliquot(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    for i in xrange(1,lim+1):
        if n % i == 0:
            if (i == n/i):
                s += i
            else:
                s += i + n/i
            
    return (s - n)

def prime_factors(n, plist):
    a = n
    f = []
    while a not in plist:
        for p in plist:
            if a % p == 0:
                a = a / p
                f.append(p)
                break
    f.append(a)
    return f
 
aq = [aliquot(x) for x in xrange(0,1001)]
prime = [x for x in xrange(0,len(aq)) if aq[x] == 1]

print prime_factors(2, prime)

s = set([])
for a in xrange(2,101):
    for b in xrange(2,101):
        l = (b * prime_factors(a, prime))
        l.sort()
        s.add(tuple(l))
        # print l
    print a, '%'
    
print len(s)