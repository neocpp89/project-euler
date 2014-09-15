#!/usr/bin/env python

def is_increasing_num(n):
    ld =  n % 10
    while n > 0:
        d = n % 10
        if (d > ld):
            return False
        ld = d
        n /= 10 
    return True

def is_decreasing_num(n):
    ld =  n % 10
    while n > 0:
        d = n % 10
        if (d < ld):
            return False
        ld = d
        n /= 10 
    return True

m = 10 ** 8
bouncy = 0
for n in xrange(1, 1+m):
    if not is_increasing_num(n) and not is_decreasing_num(n):
        bouncy += 1

    if (bouncy * 100) / n >= 99:
        print bouncy, n
        break

print bouncy, n-bouncy, n
