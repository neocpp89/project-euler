#!/usr/bin/env python
from math import sqrt
lim = 10 ** 8
sqrtlim = int(sqrt(lim))
sqrs = map(lambda x: x ** 2, range(1,sqrtlim+1))

def ispalindrome(n):
    return (str(n) == str(n)[::-1])

i = 0
ss = set([])
while i < len(sqrs):
    j = i+1
    while j < len(sqrs):
        j += 1
        s = sum(sqrs[i:j])
        if (s >= lim):
            break
        if (ispalindrome(s)):
            ss.add(s)
    i += 1

print sum(ss)
