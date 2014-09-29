#!/usr/bin/env python
from itertools import combinations

def extendtup(s):
    sl = list(s)
    if 6 in s and 9 not in s:
        sl.append(9)
    if 9 in s and 6 not in s:
        sl.append(6)
    return tuple(sorted(sl))

def can_form(n, d1, d2):
    if ((n[0] in d1 and n[1] in d2) or
        (n[0] in d2 and n[1] in d1)):
        return True
    return False

def check_squares(d1, d2):
    l = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
    for x in l:
        if not can_form(x, d1, d2):
            return False
    return True

singlesix = 0
doublesix = 0
seen = set()
possible1 = combinations(range(0,10), 6)
for x in possible1:
    possible2 = combinations(range(0,10), 6)
    oldx = x
    x = tuple(sorted(x))
    for y in possible2:
        oldy = y
        if (x,y) in seen or (y,x) in seen:
            continue
        if check_squares(extendtup(x),extendtup(y)):
            print x, y
            seen.add((x,y))
            seen.add((y,x))

print len(seen)/2 
