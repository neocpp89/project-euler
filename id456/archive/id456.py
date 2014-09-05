#!/usr/bin/env python
import itertools
import os
import math
import bigfloat
from collections import defaultdict

def readverts(f):
    P = []
    for line in f:
        P.append(tuple(map(int, line.split(','))))
    return P

def vecsub(B,A):
    return (B[0]-A[0], B[1]-A[1])

def vecdot(A,B):
    return (A[0]*B[0] + A[1]*B[1])

def origin_in_triangle(verts):
    # from http://www.blackpawn.com/texts/pointinpoly/
    A = verts[0]
    B = verts[1]
    C = verts[2]
    v0 = vecsub(C,A)
    v1 = vecsub(B,A)
    v2 = vecsub((0,0),A)

    dot00 = vecdot(v0, v0)
    dot01 = vecdot(v0, v1)
    dot02 = vecdot(v0, v2)
    dot11 = vecdot(v1, v1)
    dot12 = vecdot(v1, v2)

    invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    return (u >= 0) and (v >= 0) and (u + v < 1)
    

def angle_diff(a,b):
    diff = a - b;
    while (diff < 0.0):
        diff += 2.0 * math.pi
    while (diff >= 2.0 * math.pi):
        diff -= 2.0 * math.pi
    return diff

def build_nyk(thetas):
    nt = len(thetas)
    nyk = [0]*nt
    for i,theta in enumerate(thetas):
        if (i > 0):
            nyk[i] = nyk[i-1]
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) <= math.pi):
            nyk[i] += 1
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) >= math.pi):
            nyk[i] -= 1
        j = i+1
        while (thetas[j % nt] == theta):
            nyk[i] -= 1
            j += 1
#        print angle_diff(thetas[(i+nyk[i]) % nt], theta)
    return nyk

def listdups(l):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in l if x in seen or seen_add(x) )
    # turn the set into a list (as requested)
    return list( seen_twice )

x_n = lambda n: pow(1248, n, 32323) - 16161
y_n = lambda n: pow(8421, n, 30103) - 15051
pair_n = lambda n: (x_n(n), y_n(n))

#theta_n = lambda pair: (bigfloat.atan2(pair[1], pair[0], bigfloat.quadruple_precision))
theta_n = lambda pair: (math.atan2(pair[1], pair[0]))

#nmax = 8
#nmax = 600
nmax = 40000
#nmax = 2000000

if not (os.path.isfile(('vertices_%d.txt' % nmax))):
    P = map(pair_n, range(1,nmax+1))
    print 'Done generating verticies.'
    with open(('vertices_%d.txt' % nmax), 'w') as f:
        for point in P:
            f.write(str(point[0])+','+str(point[1])+'\n')
        f.close()
    print 'Done writing verticies to vertices_%d.txt.' % nmax
else:
    with open(('vertices_%d.txt' % nmax), 'r') as f:
        P = readverts(f)
        f.close()
    print 'Done reading verticies in vertices_%d.txt.' % nmax

n = nmax+1
C = (2 * n - 3) * (n - 1) * (n - 2) / 12
thetas = map(theta_n, P)
thetas.sort()
thetas = map(lambda x: thetas[x], range(0,len(thetas)))
print 'Done mapping theta.'
theta_dict = defaultdict(int)
for t in thetas:
    theta_dict[t] += 1
dup_theta = listdups(thetas)
unique_theta = list(set(thetas))
for x in dup_theta:
    print theta_dict[x]
#n = len(unique_theta)+1
#C = (2 * n - 3) * (n - 1) * (n - 2) / 12
print 'Initial C =', C
nyk = build_nyk(thetas)
print 'Done building nyk.'
nsq = map(lambda x: x ** 2, nyk)
C = C - (sum(nsq) / 2)
print 'Final C =', C

