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

lim = 10 ** 6
try:
    with open('aliquots.txt') as f:
        aliquots = map(int, f)
except:
    aliquots = map(aliquot, range(0,1+lim))
    for x in aliquots:
        print x
    exit()

amicable = [0]*(1+lim)
chain = 0

for i in range(0,1+lim):
    if (amicable[i] != 0):
        continue
    start = aliquots[i]
    seen = set([])
    x = start
    while x not in seen:
        if (x < (lim + 1)):
            seen.add(x)
            x = aliquots[x]
        else:
            break
        if (x == start):
            chain += 1
            amicable[i] = chain
            for s in seen:
                amicable[s] = chain
            break
           
t = zip(aliquots, amicable, range(0, 1 + lim)) 
ac = filter(lambda x: x[1] != 0, t)

m = 0
ml = 0
for l in range(0, chain+1):
    w = len(filter(lambda a: a[1] == l, ac))
    if (w > m):
        m = w
        ml = l

print filter(lambda a: a[1] == ml, ac)[0][2]
