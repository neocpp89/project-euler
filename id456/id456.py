#!/usr/bin/env python
import itertools
import os
import math
import bigfloat
from collections import defaultdict

#bfcontext = bigfloat.quadruple_precision
bfcontext = bigfloat.precision(1024)

def readverts(f):
#    P = []
#    for line in f:
#        P.append(tuple(map(int, line.split(','))))
    P = map(lambda line: tuple(map(int, line.split(','))), f)
    return P

def angle_diff(a,b):
    diff = a - b;
    twopi = 2.0 * math.pi
    while (diff < 0.0):
        diff += twopi
    while (diff >= twopi):
        diff -= twopi
    return diff

def bfangle_diff(a,b):
    diff = a - b;
    twopi = 2.0 * bigfloat.const_pi(bfcontext)
    while (diff < 0.0):
        diff += twopi
    while (diff >= twopi):
        diff -= twopi
    return diff

def build_nyk(thetas):
    nt = len(thetas)
    nyk = [0]*nt
    pi = math.pi
    for i,theta in enumerate(thetas):
        if (i > 0):
            nyk[i] = nyk[i-1] - 1
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) < pi or thetas[(i+nyk[i]+1) % nt] == thetas[(i+nyk[i]) % nt]):
            nyk[i] += 1
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) >= pi or thetas[(i+nyk[i]-1) % nt] == thetas[(i+nyk[i]) % nt]):
            nyk[i] -= 1
    return nyk

def bfbuild_nyk(thetas):
    nt = len(thetas)
    nyk = [0]*nt
    pi = bigfloat.const_pi(bfcontext)
    for i,theta in enumerate(thetas):
        if (i > 0):
            nyk[i] = nyk[i-1] - 1
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) < pi or thetas[(i+nyk[i]+1) % nt] == thetas[(i+nyk[i]) % nt]):
            nyk[i] += 1
        while (angle_diff(thetas[(i+nyk[i]) % nt], theta) >= pi or thetas[(i+nyk[i]-1) % nt] == thetas[(i+nyk[i]) % nt]):
            nyk[i] -= 1
    return nyk

def build_nyk_ext(thetas, dups):
    nt = len(thetas)
    nyk_idx = [0]*nt
    nyk = [0]*nt
    pi = math.pi
    for i,theta in enumerate(thetas):
        if (i > 0):
            nyk_idx[i] = nyk_idx[i-1] - 1
            nyk[i] = nyk[i-1] - dups[i-1]
        while ((angle_diff(thetas[(i+nyk_idx[i]) % nt], theta) - pi) <= 0.0):
            nyk[i] += dups[(i+nyk_idx[i]) % nt]
            nyk_idx[i] += 1
        while ((angle_diff(thetas[(i+nyk_idx[i]) % nt], theta) - pi) > 0.0):
            nyk_idx[i] -= 1
            nyk[i] -= dups[(i+nyk_idx[i]) % nt]
    return nyk, nyk_idx

def bfbuild_nyk_ext(thetas, dups):
    nt = len(thetas)
    nyk_idx = [0]*nt
    nyk = [0]*nt
    pi = bigfloat.const_pi(bfcontext)
    for i,theta in enumerate(thetas):
        if (i > 0):
            nyk_idx[i] = nyk_idx[i-1] - 1
            nyk[i] = nyk[i-1] - dups[i-1]
        while (angle_diff(thetas[(i+nyk_idx[i]) % nt], theta) < pi):
            nyk[i] += dups[(i+nyk_idx[i]) % nt]
            nyk_idx[i] += 1
        while (angle_diff(thetas[(i+nyk_idx[i]) % nt], theta) > pi):
            nyk_idx[i] -= 1
            nyk[i] -= dups[(i+nyk_idx[i]) % nt]
    return nyk, nyk_idx

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

#theta_n = lambda pair: (bigfloat.atan2(pair[1], pair[0], bfcontext))
theta_n = lambda pair: (math.atan2(pair[1], pair[0]))

#nmax = 8
#nmax = 600
#nmax = 40000
#nmax = 2000000
nvals = [8,600,40000,2000000]
solns = [20,8950634,2666610948988,0]

for k,nmax in enumerate(nvals):
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

    n = nmax
    thetas = map(theta_n, P)
    thetas.sort()
    print 'Done mapping theta.'
#    theta_dict = defaultdict(int)
#    for t in thetas:
#        theta_dict[t] += 1
#    dup_theta = listdups(thetas)
#    unique_thetas = sorted(list(set(thetas)))
#    duptuples = [(x, theta_dict[x]-1, unique_thetas.index(x)) for x in dup_theta] # number of additional pts at x
#    duptuples.sort(key=lambda p: p[2])
#    dups = map(lambda x: theta_dict[x], unique_thetas)
#    nyk, nyk_idx = build_nyk_ext(unique_thetas, dups)
#    nyk, nyk_idx = bfbuild_nyk_ext(unique_thetas, dups)
    nykprime = build_nyk(thetas)
#    nykprime = bfbuild_nyk(thetas)
    print 'Done building nyk.'
#    nykstar = [(nk-dups[i]+1) for i, nk in enumerate(nyk)]
#    T = [(nk*(n-nk-1) - (nk*(nk-1)/2)) for i, nk in enumerate(nyk)]
    T = [0]*len(thetas)
    dupc = 1
    C = 0
    for i, nk in enumerate(nykprime):
        if (i < (len(thetas)-1) and thetas[i] >= thetas[(i+1)]):
            dupc += 1
        else:
            T[i] = nk*(n-nk-dupc) - dupc*(nk*(nk-1)/2)
            dupc = 1
    C = C + sum(T)/3
    print 'N =', nmax
    print 'Final C =', C, 'Soln =', solns[k], 'Diff =', abs(C-solns[k])

