#!/usr/bin/env python

def sdigits(i):
    return sorted(list(str(i)))

i = 100
while True:
    i += 1
    s = sdigits(i)
    if (s == sdigits(2*i) and
        s == sdigits(3*i) and
        s == sdigits(4*i) and
        s == sdigits(5*i) and
        s == sdigits(6*i)):
            print i
            break
