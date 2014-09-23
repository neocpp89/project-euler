#!/usr/bin/env python
lim = 10 ** 9

c = 0
for x in xrange(0, 1+lim):
    if (x % 10) == 0:
        continue
    p = map(lambda d: int(d) % 2 == 1, list(str(int(str(x)[::-1])+x)))
    if all(p):
        c += 1
        print x, c
