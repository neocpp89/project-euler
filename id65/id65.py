#!/usr/bin/env python

def gen_num(n):
    a = 2
    yield a
    b = 3
    yield b
    for x in range(0, n-2):
        f = 1
        if (x % 3 == 0):
            f = 2 * (1 + (x / 3))
        c = f * b + a
        yield c
        a = b
        b = c

def gen_den(n):
    a = 1
    yield a
    b = 1
    yield b
    for x in range(0, n-2):
        f = 1
        if (x % 3 == 0):
            f = 2 * (1 + (x / 3))
        c = f * b + a
        yield c
        a = b
        b = c

print sum(map(int, list(str(list(gen_num(100))[-1]))))
