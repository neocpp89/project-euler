#!/usr/bin/env python
import math

xo = 0 
yo = 0

contains_origin = 0
with open('triangles.txt') as f:
    pl = map(lambda x: map(float, x.split(',')), f)
    tris = map(lambda x: [(x[0]-xo,x[1]-yo),(x[2]-xo,x[3]-yo),(x[4]-xo,x[5]-yo)] ,pl)
    # print tris
    for points in tris:
        angles = sorted(map(lambda x: math.pi + math.atan2(x[1], x[0]), points))
        diffs = filter(lambda y: y != 0, map(lambda x: x - angles[0], angles))
        if (diffs[0] > math.pi):
            continue
        if (diffs[1] > math.pi and (diffs[1] - diffs[0]) <= math.pi):
            print points
            contains_origin += 1

print contains_origin

