#!/usr/bin/env python
import math
import gmpy
import numpy

def is_square(n):
    x = int(math.sqrt(n))
    return (n == x * x)

'''
t = 10 ** 12
while True:
    r = 1 + 2 * t ** 2 - 2 * t
    if (gmpy.is_square(r)):
        if (r % 2 == 1):
            print int(1+math.sqrt(r))/2
    t += 1
'''

def seq_A001653(n=(10 ** 13)):
    a = 1
    yield a
    b = 5
    yield b
    r = 0
    while r < n:
        r = 6 * b - a
        yield r
        a = b
        b = r



nums = seq_A001653()

tr = next(nums)
while True:
    tr = next(nums)
    s = tr ** 2
    if (not gmpy.is_square(2 * s - 1)):
        continue
    t = (1 + gmpy.sqrt(2 * s - 1)) / 2
    r = 1 + 2 * t ** 2 - 2 * t
    if (gmpy.is_square(r)):
        if (r % 2 == 1):
            print int(1+gmpy.sqrt(r))/2, t
            if (t > 10 ** 12):
                break
            

