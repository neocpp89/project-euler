#!/usr/bin/env python
import numpy

def f(x):
    return (1e-9 * numpy.floor(numpy.power(2, 30.403243784 - x ** 2)))

#print f(-1)
#print f(f(-1))
#print f(f(f(-1)))
#print f(f(f(f(-1))))

#print (f(-1) + f(f(-1)))

#print f(f(f(-1))) + f(f(f(f(-1))))

up = f(-1)
u = f(up)

for i in xrange(1,2000):
    print(u + up)
    up = u
    u = f(up)

