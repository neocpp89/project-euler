#!/usr/bin/env python

def intsqrt(n):
    x = n
    xn = n / 2
    while (x > xn):
        x = xn
        xn = (x + n / x) / 2
    return x

def has_int_area(a,b,c):
    p = (a + b + c)
    if (p % 2 == 1):
        return False
    s = p / 2
    asq = s*(s-a)*(s-b)*(s-c)
    a = intsqrt(asq)
    return (a * a == asq)

def intarea_p(a):
    qq = (a - 1) * (3 * a + 1)
    q = intsqrt(qq)
    if (q * q == qq):
        if ((q * (a - 1)) % 4 == 0):
            return True
    return False
    
def intarea_n(a):
    qq = (a + 1) * (3 * a - 1)
    q = intsqrt(qq)
    if (q * q == qq):
        if ((q * (a + 1)) % 4 == 0):
            return True
    return False

'''
lim = 10 ** 9
ptotal = 0
for p in xrange(4, 1+lim):
    if (p % 3 == 0):
        continue
    a = p / 3
    if (p % 3 == 2):
        a += 1
    c = p - (2 * a)
    if has_int_area(a,a,c):
        print a, a, c
        ptotal += p
'''
lim = 1 + (10 ** 9 / 3)
ptotal = 0
for a in xrange(5, 1+lim, 4):
    if intarea_n(a):
        ptotal += 3*a - 1
        print a, a, a - 1, 3*a - 1, ptotal
    if intarea_p(a):
        ptotal += 3*a + 1
        print a, a, a + 1, 3*a + 1, ptotal
print ptotal
