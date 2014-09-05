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

def left(x):
    if (x == 0):
        return True
    return ((aliquot(x) == 1) and left(x / 10))

def right(x):
    if (x == 0):
        return True
    power = 10 ** int(math.floor(math.log10(x)))
    firstdigit = x / power
    return ((aliquot(x) == 1) and right(x - firstdigit * power))
        

largest = 1000000

aq = [aliquot(x) for x in range(11, 1+largest)]
aa,pr = zip(*filter(lambda tup: tup[0] == 1, zip(aq, range(11, 1+largest))))
prime = [1]
prime.extend(list(pr))
print 'prime:', prime

trunc_primes = []
for p in prime:
    if (left(p) and right(p)):
        trunc_primes.append(p)
        print p

    if len(trunc_primes) == 11:
        print 'Sum:', sum(trunc_primes)
        break
