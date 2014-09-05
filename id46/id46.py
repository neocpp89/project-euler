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

largest = 10000

aq = [aliquot(x) for x in range(1, 1+largest)]
aa,pr = zip(*filter(lambda tup: tup[0] == 1, zip(aq, range(1, 1+largest))))
prime = [1]
prime.extend(list(pr))
print 'prime:', prime

square = list(x * x for x in range(1, int(math.ceil(math.sqrt(1+largest)))))
print 'square:', square

for i in range(1, largest/2):
    trial = 2 * i  + 1
    if (trial in prime):
        continue
    found = False
    filtpr = filter(lambda x: x <= trial, prime)
    filtsq = filter(lambda x: x <= (i+1), square)
   

    for p in filtpr:
        for s in filtsq:
            i# print p, s
            if (p + 2 * s == trial):
                found = True

    if (found == False):
        print 'Composite', trial, 'violates alt. GC.'
        break
