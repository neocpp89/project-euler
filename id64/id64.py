#!/usr/bin/env python
from math import sqrt

def issquare(n):
    a = int(sqrt(n))
    return n == a * a

'''
def continued_fraction_sqrt(n):
    s = sqrt(n)
    a = int(s)
    yield a
    while True:
        s = 1 / (s - a)
        a = int(s)
        yield a
'''

def continued_fraction_sqrt(n):
    m = 0
    d = 1
    a = int(sqrt(n))
    yield a
    while True:
        m = d*a - m
        d = (n - m*m) / d
        a = int((sqrt(n) + m) / d)
        yield a

lim = 10000
c = 0
for x in range(1, 1+lim):
    if (issquare(x)):
        continue

    f = continued_fraction_sqrt(x)
    a = f.next()
    b = a
    seq = 0

    while b != 2*a:
        b = f.next()
        seq += 1

    print x, seq
    if (seq % 2 == 1):
        c += 1

print c

