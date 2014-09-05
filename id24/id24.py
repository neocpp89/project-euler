#!/usr/bin/env python

# s = '0123'
# nums = [int(x) for x in str]
# for i in xrange()

def fact(f):
    return reduce(lambda x,y: x*y, range(1,f+1), 1)

n = 999999
nCh = 10

rem = n
s = [int(x) for x in '0123456789']
ns = []
for i in xrange(1,nCh+1):
    f = fact(nCh-i);
    div = rem / f
    rem = rem % f
    ns.append(s[div])
    s.pop(div)
    print nCh-i, div, rem
    
print reduce(lambda x,y: x+y, [str(c) for c in ns], '')