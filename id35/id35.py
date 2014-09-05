#!/usr/bin/env python
import math

def aliquot(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    for i in xrange(1,lim+1):
        if n % i == 0:
            if (i == n/i):
                s += i
            else:
                s += i + n/i
            
    return (s - n)

def rotate_string(s):
    s_rot = s[-1] + s[:-1]
    return s_rot

aq = [aliquot(x) for x in xrange(0,int(1e6))]
prime = [x for x in xrange(0,len(aq)) if aq[x] == 1]

plist = []
for p in prime:
    s = str(p)
    w = 1
    for i in xrange(0,len(s)):
        s = rotate_string(s)
        if (aq[int(s)] != 1):
            w = 0
    if (w == 1):
        print p
        plist.append(p)

print '#', len(plist)

