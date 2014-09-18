#!/usr/bin/env python

def intsqrt(n):
    x = n
    xn = n / 2
    while (x > xn):
        x = xn
        xn = (x + n / x) / 2
    return x

def is_perfect_sq(n):
    x = intsqrt(n)
    return (x * x == n)

def sqrtdigitsum(n,numdigits=100):
    return sum(map(int, list(str(intsqrt(n * 10 ** 200)))[:numdigits]))

z = [y for y in range(2,101) if not is_perfect_sq(y)]
print z

print sum(map(lambda x: sqrtdigitsum(x), z))
