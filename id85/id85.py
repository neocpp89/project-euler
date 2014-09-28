#!/usr/bin/env python

l = 10 **  2
d = {}
for X in range(1, l):
    for Y in range(X, l):
        nr = 0
        for x in range(0, X):
            for y in range(0, Y):
                nr += (X-x)*(Y-y)
        d[(X,Y)] = nr

best = 0
ab = 10000
for k in d:
    if (abs(2*10**6 - d[k]) < ab):
        best = k
        ab = abs(2*10**6 - d[k])

print best, ab, d[best]

