#!/usr/bin/env python

def fib(n):
    a = 1
    yield a
    b = 1
    yield b
    for i in range(0, n-2):
        c = a + b
        yield c
        a = b
        b = c

digits = map(str, range(1,10))

def firstpandsgital(sn):
    s = sn[:9]
    return sorted(s) == digits
def lastpandigital(sn):
    s = sn[-9:]
    return sorted(s) == digits
def bothendspandigital(sn):
    return lastpandigital(sn)

i = 1
for x in fib(1000000):
    # last digits pandigital
    if (sorted(str(x % (10 ** 9))) == digits):
        if firstpandsgital(str(x)):
            print i
            break
    i += 1
