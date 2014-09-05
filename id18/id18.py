#!/usr/bin/env python
import copy

def collapse(top, bottom):
    ntop = copy.deepcopy(top)
    for i in xrange(0, len(top)):
        m = max(bottom[i], bottom[i+1])
        ntop[i] += m
    return ntop

with open('tri.txt', 'r') as file:
    triangle = []
    for line in file:
        triangle.append(map(int, line.split()))
    
    triangle.reverse()
    
    while len(triangle) != 1:
        if (len(triangle) > 1):
            n = collapse(triangle[1], triangle[0])
            triangle.pop(0)
            triangle[0] = n
        print triangle