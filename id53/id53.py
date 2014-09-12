#!/usr/bin/env python
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

count = 0
for n in range(0, 101):
    for r in range(0, 1+n/2):
        f = nCr(n, r)
        if (f > 1000000):
            count += (n-2*r)+1
            break

print count

