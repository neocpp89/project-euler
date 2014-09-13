#!/usr/bin/env python

m = 100
dsum = 0
for a in range(1, 1+m):
    for b in range(1, 1+m):
        ds = sum(map(int, list(str(a ** b))))
        if (ds > dsum):
            dsum = ds
            print a, b

print dsum
