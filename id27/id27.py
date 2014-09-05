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

def quad_function(a,b,n):
    return n ** 2 + a * n + b 
    
a = [aliquot(x) for x in xrange(0,1001)]
prime = [x for x in xrange(0,len(a)) if a[x] == 1]
print prime

best_tuple = (1,41)
best_nmax = 39
prod = 41
for b in prime:
    for a in xrange(-1000, 1001):
        n = 0
        while quad_function(a,b,n) in prime:
            n += 1
        n -= 1
        if (n > best_nmax):
            best_nmax = n
            best_tuple = (a,b)
            prod = a*b
print best_nmax
print best_tuple
print prod
