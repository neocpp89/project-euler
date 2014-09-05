#!/usr/bin/env python

f = range(1,101)

print f

f5 = filter(lambda x: x % 5 == 0, f)
f2 = filter(lambda x: x % 2 == 0 and x % 10 != 0, f)
fn25 = filter(lambda x: x % 5 != 0 and x % 2 != 0, f)

print fn25, f2, f5

for i in xrange(0, len(f5)):
    f2[i] = f2[i]*f5[i]
    while (f2[i] % 10 == 0):
        f2[i] = f2[i] / 10
    f5[i] = 1
    
print fn25, f2, f5

f = filter(lambda x: x != 1, fn25 + f2 + f5)
print f

print sum([int(x) for x in str(reduce(lambda x,y: x*y, f, 1))])
