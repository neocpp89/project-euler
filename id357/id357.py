#!/usr/bin/env python
import math

def isprime(n):
    if (n == 0 or n == 1):
        return False
    if (n == 2):
        return True
    if (n == 3):
        return True

    if (n % 6 != 1 and n % 6 != 5):
        return False
    d = 2
    while d*d <= n:
        if (n % d) == 0:
            return False
        d += 1
    return True

def divsiors(n):
    s = int(math.sqrt(n))
    d = []
    for i in range(1, s+1):
        if n % i == 0:
            d.append(i)
            d.append(n / i)
    return d

def need_to_check(n):
    s = int(math.sqrt(n))
    d = []
    for i in range(1, s+1):
        if n % i == 0:
            d.append(i + (n / i))
    return d

print need_to_check(30)

upto = 100000000

s = 0
for i in range(1, upto + 1):
    print i
    l = need_to_check(i)
    if all(map(isprime, l)):
        s += i
print s
