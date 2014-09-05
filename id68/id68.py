#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:16:43 2014

@author: sdunatunga
"""

import itertools

# threegon = range(1,7)
fivegon = range(1,11)

# perms = itertools.permutations(threegon)
perms = itertools.permutations(fivegon)
s = set([])

for p in perms:
    # g = [[p[0], p[1], p[2]]]
    # g.append([p[3], p[2], p[4]])
    # g.append([p[5], p[4], p[1]])

    #only want 16 digit -> 10 in positions 0,3,5,7,9 only
    tenidx = p.index(10)
    valididx = [0,3,5,7,9]
    if (tenidx not in valididx):
        continue

    g = [[p[0], p[1], p[2]]]
    g.append([p[3], p[2], p[4]])
    g.append([p[5], p[4], p[6]])
    g.append([p[7], p[6], p[8]])
    g.append([p[9], p[8], p[1]])
    
    gsum = map(sum, g)
    sumsame = map(lambda x: x == gsum[0], gsum)
    if all(sumsame):
        # print gsum[0], ":", g
        minel = g[0][0]
        minelidx = 0
        for idx, el in enumerate(g):
            if (el[0] < minel):
                minel = el[0]
                minelidx = idx 
        gprime = []
        for i in range(0, len(g)):
            gprime.append(g[(i + minelidx) % len(g)])
        chain = itertools.chain.from_iterable(gprime)
        flat = list(chain)
        # key = str(gsum[0])+":"+"".join(map(str, flat))
        # print key
        key = (int("".join(map(str, flat))), gsum[0])
        print key
        s.add(key)
        
for it in sorted(s):
    print it
