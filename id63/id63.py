#!/usr/bin/env python
import math

c = 0
p = 1
logs = map(math.log10, range(1,10))

while p < (1+(1/(1-logs[-1]))):
    c += len(filter(lambda x: int(p*x) + 1 == p, logs))
    p += 1

print c
