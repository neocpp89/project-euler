#!/usr/bin/env python
import math

def is_square(apositiveint):
  if (apositiveint == 1):
    return True
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def pentagonal_number(n):
    return (n * (3 * n - 1) / 2)

n = range(1,10000)
pn = map(pentagonal_number, n)

save = []
for i,p in enumerate(pn):
    ss = map(lambda x: x + p, pn)
    for j,s in enumerate(ss):
        tmp = 24 * s + 1
        if is_square(tmp) == False:
            continue
        if (math.sqrt(tmp) % 6 != 5):
            continue
#        print i, j
        ds = abs(pn[i]-pn[j])
        tmp = 24 * ds + 1
        if is_square(tmp) == False:
            continue
        if (math.sqrt(tmp) % 6 != 5):
            continue
        print i, j, 'D =', ds
        save.append( (i,j,s,ds) )

print save
