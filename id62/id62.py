#!/usr/bin/env python

lim = 10 ** 4

cubes = map(lambda x: x ** 3, range(0, 1+lim))

d = dict()
for c in cubes:
    k = tuple(sorted(list(str(c))))
    if k not in d:
        d[k] = [c]
    else:
        d[k].append(c)
for k in d:
    if (len(d[k]) == 5):
        print sorted(d[k])
