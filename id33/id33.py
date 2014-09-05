#!/usr/bin/env python

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (a == b and b == c):
                continue
            resid = 10 * a *  (c - b) - c * (a - b)
            if (resid == 0):
                print a,b,c
