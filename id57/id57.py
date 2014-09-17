#!/usr/bin/env python

import math

def generate_numerator(n=1000):
    a = 3
    yield a
    b = 7
    yield b
    for i in range(0,n-2):
        c = 2 * b + a
        yield c
        a = b
        b = c

def generate_denominator(n=1000):
    a = 2
    yield a
    b = 5
    yield b
    for i in range(0,n-2):
        c = 2 * b + a
        yield c
        a = b
        b = c

def count_digits(n):
    c = 0
    while n > 0:
        n /= 10
        c += 1
    return c

n = generate_numerator(1000)
d = generate_denominator(1000)

cn = map(count_digits, n)
cd = map(count_digits, d)

print sum([1 for t in map(lambda x: x[0] > x[1], zip(cn, cd)) if t == True])
