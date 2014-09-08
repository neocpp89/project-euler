#!/usr/bin/env python

def ispalindrome(n):
    s = str(n)
    return (s[::-1] == s)

def reversenum(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n / 10
    return r

def islychrel(n, depth=0, known=None):
    if (depth == 50):
        if (known is not None):
            known[n] = True
        return True

    if (known is not None and n in known):
        return known[n]

    nextn = n + reversenum(n)

    if (ispalindrome(nextn)):
        if (known is not None):
            known[n] = False
        return False
    else:
        return islychrel(nextn, depth+1, known)

lychrel = filter(islychrel, range(0,10001))

print lychrel, len(lychrel)
