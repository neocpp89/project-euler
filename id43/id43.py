#!/usr/bin/env python

import itertools

digits = range(0,10)

csum = 0
for p in itertools.permutations(digits):
    num = int("".join(map(str,list(p))))
#    print num
    div2 = int("".join(map(str,list(p[1:4]))))
    if (div2 % 2 != 0):
        continue
#    print div2
    div3 = int("".join(map(str,list(p[2:5]))))
    if (div3 % 3 != 0):
        continue
    div5 = int("".join(map(str,list(p[3:6]))))
    if (div5 % 5 != 0):
        continue
    div7 = int("".join(map(str,list(p[4:7]))))
    if (div7 % 7 != 0):
        continue
    div11 = int("".join(map(str,list(p[5:8]))))
    if (div11 % 11 != 0):
        continue
    div13 = int("".join(map(str,list(p[6:9]))))
    if (div13 % 13 != 0):
        continue
    div17 = int("".join(map(str,list(p[7:10]))))
    if (div17 % 17 != 0):
        continue
    print 'passed', num
    csum = csum + num

print csum
