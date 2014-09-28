#!/usr/bin/env python
from math import log

'''
lim = 10 ** 10
c = 0
for x in xrange(11, 1+lim):
    s = sum(map(int, str(x)))
    if (s > 1):
        q = int(log(x, s))
        if s ** q == x:
            c += 1
            print c, x
'''

c = 0
n = set()
for b in range(2,401):
    for e in range(2,31):
        s = b ** e
        if b == sum(map(int, str(s))):
            n.add(s)

for x in enumerate(sorted(list(n))):
    print x
