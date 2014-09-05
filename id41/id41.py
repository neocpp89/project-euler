#!/usr/bin/env python
import math
import itertools

#def to_base_nine(n):
#    while n != 0:
#        s = s + str(n % 9)
#    return s

#def from_base_nine(s):
#    n = 0
#    for c in s:
#        n = 9*n + int(c)
#    return n

#s = ''
#for i in xrange(1,500000):
#    s = s + str(i);

#for i in [1, 10, 100, 1000, 10000, 100000,1000000]:
#    print s[i-1]

#print from_base_nine('1234')

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

s = ''
ss = []
for i in range(1,10):
    s = s + str(i)
    ss.append(s)

ss.reverse()
print ss

maxpp = 0

for elem in ss:
    s = list(str(elem))
    perms = itertools.permutations(s)
    for p in perms:
#        print p
        pp = int("".join(p))
        if (aliquot(pp) == 1):
            print pp
            if (pp >= maxpp):
                maxpp = pp
    if (maxpp > 0):
        break

print maxpp
