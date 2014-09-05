#!/usr/bin/env python
import math

i = 0
while (i < 1e8):
    i = i + 1
    num = i
    d_prev = num % 10
    c = math.factorial(d_prev)
    while (num / 10 != 0):
        num = num / 10
        d_prev = num % 10
        c = c + math.factorial(d_prev)
    if (c == i):
        print '\n!!!:',c
    else:
        print "\r",i,"",

