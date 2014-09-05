#!/usr/bin/env python

import csv
import numpy

def prop_up(M, x, y):
    M[x,y-1] += M[x,y]

def prop_left(M, x, y):
    M[x-1,y] += M[x,y]

def clear(M, x, y):
    M[x,y] = 0

with open('p081_matrix.txt') as f:
    r = csv.reader(f, delimiter=',')
    mat = numpy.array(map(lambda x: map(int, x), r))
    print mat
    N = len(mat)


