#!/usr/bin/env python
import sys

def partition_function(n,known={},m=10**7):
    if (n == 0):
        known[n] = 1
        return 1
    if (n < 0):
        return 0
    s = 0
    for k in range(1,n+1):
        leftn = n - (k*(3*k-1))/2
        rightn = n - (k*(3*k+1))/2
        if leftn in known:
            left = known[leftn]
        else:
            left = partition_function(leftn, known)
        if rightn in known:
            right = known[rightn]
        else:
            right = partition_function(rightn, known)
        s += (((-1)**(k+1) * (left + right))) % m
    if n not in known:
        known[n] = s % m
    return s

# dont include 'q + 0'
lim = 10 ** 6
dk = {}
for q in range(1, 1+lim):
    p = partition_function(q, dk)
    print q 
    if (p % 10 ** 6 == 0):
        print '!', p, q
        break
