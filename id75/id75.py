#!/usr/bin/env python
import math
import numpy as np

def is_square(s):
    if (s < 0):
        return False
    x = int(math.sqrt(s))
    return (s - x * x == 0)

def get_ra_triplets(l):
    s = []
    for c in range(l/3, l/2):
        for a in range(1, 1+(l-c)/2):
            bsq1 = c * c - a * a
            bsq2 = (l-(c+a)) ** 2
            if (bsq1 == bsq2):
                s.append((a,l-(c+a),c))
    return s

def num_ra_triplets(l):
    s = 0
    for c in range(l/3, l/2):
        for a in range(1, 1+(l-c)/2):
            bsq1 = c * c - a * a
            bsq2 = (l-(c+a)) ** 2
            if (bsq1 == bsq2):
                s += 1
    return s

def gen_triples(start=(3,4,5), stopfunc=None, running=[]):
    if (stopfunc is not None):
        if stopfunc(start):
            return None
    running.append(start)
    A = np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
    B = np.array([[1,2,2],[2,1,2],[2,2,3]])
    C = np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
    children = [tuple(A.dot(start)), tuple(B.dot(start)), tuple(C.dot(start))]
    for x in children:
        gen_triples(x, stopfunc, running)
    return running


#print get_ra_triplets(12)
#print get_ra_triplets(24)
#print get_ra_triplets(30)
#print get_ra_triplets(36)
#print get_ra_triplets(120)

#m = 120
#c = 0
#for L in range(12,m+1):
#    s = num_ra_triplets(L)
#    if (s == 1):
#        c += 1
#        print L
#print '#', c


m = 1500000
pt = gen_triples(stopfunc = lambda x: sum(x) >= m)
#print sorted(pt)
l = filter(lambda x: x <= m, map(sum, pt))
d = {}
for x in l:
    for y in range(x, 1+m, x):
        if y in d:
            d[y] += 1
        else:
            d[y] = 1

c = 0
for k in d:
    if d[k] == 1:
        c += 1
print c
#print l
#c = 0
#for L in set(l):
#    if l.count(L) == 1:
#        c += 1
#print c

'''
ll = []
for a in range(1, m):
    # print a
    for b in range(a+1, 1+m-a):
        csq = a ** 2 + b ** 2
        if (is_square(csq)):
            l = int(math.sqrt(csq) + (a+b))
            if (l > m):
                break
            ll.append(l)

s = set(ll)
c = 0
for l in sorted(list(s)):
    if ll.count(l) == 1:
        c += 1
        # print l
print '#', c
'''
