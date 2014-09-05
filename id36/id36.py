#!/usr/bin/env python

nums = range(1,int(1e6)+1)
strs = map(str, nums)

print 'made strings'

candidates = []
for s in strs:
    if (s[::-1] == s):
        candidates.append(int(s))

print 'found candidates'

binstrs = map(lambda x: bin(x)[2:], candidates)

dbpalindromes = []
for b in binstrs:
    if (b[::-1] == b):
        dbpalindromes.append(b)

print 'found double base palindromes'

print sum(map(lambda x: int('0b'+x, base=0), dbpalindromes))

