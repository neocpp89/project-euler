#!/usr/bin/env python
import math

f = map(math.factorial, range(0, 10))

def digitfacsum(n):
    return sum(map(lambda x: f[x], map(int, list(str(n)))))

def chain_length(n):
    s = set([n])
    x = digitfacsum(n)
    while (x not in s):
        s.add(x)
        x = digitfacsum(x)
    return len(s)

lim = 10 ** 6
cl = map(chain_length, range(0, 1+lim))

print len(filter(lambda x: x == 60, cl))

'''
lim = 10 ** 6
cyclen = [0]*(1+lim)

for i in range(0, 1+lim):
    if (cyclen[i] == 0):
        x = digitfacsum(i)
        if (x < i):
            cyclen[i] = 1 + cyclen[x]
            continue
        s = set([i])
        while (x not in s):
            s.add(x)
            x = digitfacsum(x)
        cl = len(s)
        cyclen[i] = cl

print len(filter(lambda x: x == 60, cyclen))
'''
