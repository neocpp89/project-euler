#!/usr/bin/env python
from math import sqrt

def kdeqn(k, d):
    return -k**2 + 6*k*d - 5*d**2

def sdeqn(s, d):
    return (s+2*d)**2 - (s+d)**2 - s**2

def introots(a,b,c):
    d = b**2 - 4*a*c
    if (d < 0):
        return (0, 0)
    s = int(sqrt(d))
    p = (-b + s) / (2*a)
    n = (-b - s) / (2*a)
    return (p, n)

lim = 10 ** 6
s = 0
f = {}
while True:
    s += 1
    pr, nr = introots(3, 2*s, -s**2)
    d = pr-1
    na = 0
    while True:
        d += 1
        x = (s,d)
        t = sdeqn(*x)
        if t <= 0:
            continue
        if t > lim:
            break
        print x, t, pr, nr
        na += 1
        if t in f:
            f[t].append(x)
        else:
            f[t] = [x]
    if s > 3 * lim / 4:
        break

print len(filter(lambda x: x == 10, map(lambda x: len(f[x]), f)))
'''
def introots(a,b,c):
    d = b**2 - 4*a*c
    if (d < 0):
        return (0, 0)
    s = int(sqrt(d))
    p = (-b + s) / (2*a)
    n = (-b - s) / (2*a)
    return (p, n)

lim = 10 ** 6

c = 0
for n in range(1, 1+lim):
    #ll = []
    nsol = 0
    for d in range(1, n):
        kp, kn = introots(1, -6*d, 5*d**2 + n)
        if (kp > 2*d and kdeqn(kp, d) == n):
            #ll.append((kp, d))
            nsol += 1
        if (kn != kp and kn > 2*d and kdeqn(kn, d) == n):
            #ll.append((kn, d))
            nsol += 1
    #print n, ll
    #if (len(ll) == 2):
    print n, nsol
    if nsol == 10:
        c += 1
print c
'''


