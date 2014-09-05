#!/usr/bin/env python
from __future__ import print_function
import csv
import numpy
import sys

def prop_up(M, x, y):
    M[x,y-1] += M[x,y]

def prop_left(M, x, y):
    M[x-1,y] += M[x,y]

def clear(M, x, y):
    M[x,y] = 0


with open(sys.argv[1]) as f:
    r = csv.reader(f, delimiter=',')
    mat = numpy.array(map(lambda x: map(int, x), r))
    print(mat) 
    N = len(mat)
    l = []

    for rcsum in range(0, 2*N-1):
        deltas = range(0, rcsum+1)
        first = (0, rcsum)
        coords = filter(lambda coords: (coords[0] >= 0 and coords[0] < N and coords[1] >= 0 and coords[1] < N),
                list((delta + first[0], -delta + first[1]) for delta in deltas))
        l.append(coords)

#    map(lambda x: print(x), l)
    numlists = map(lambda r: map(lambda coord: mat[coord], r), l)[::-1]
    working = map(lambda r: map(lambda coord: numpy.inf,r), l)[::-1]
#    map(lambda x: print(x), numlists)

#    print(map(lambda x: len(x), l))

    for r in xrange(0, 2*N-2):
        # map(lambda x: print(x), working)
        l = numlists[r]
        if (r < N-1):
            for j in xrange(0, len(l)):
                if (working[r][j] == numpy.inf):
                    working[r][j] = l[j]
                s = working[r][j]
                
                if (working[r+1][j] == numpy.inf) or (s + numlists[r+1][j] < working[r+1][j]):
                    working[r+1][j] = numlists[r+1][j] + s
                j = j + 1
                if (j < len(working[r+1])):
                    if (working[r+1][j] == numpy.inf) or (s + numlists[r+1][j] < working[r+1][j]):
                        working[r+1][j] = numlists[r+1][j] + s
        else:
            for j in xrange(0, len(l)):
                if (working[r][j] == numpy.inf):
                    working[r][j] = l[j]
                s = working[r][j]
                if (j >= 0 and j < len(working[r+1])):
                    if (working[r+1][j] == numpy.inf) or (s + numlists[r+1][j] < working[r+1][j]):
                        working[r+1][j] = numlists[r+1][j] + s
                j = j - 1
                if (j >= 0 and j < len(working[r+1])):
                    if (working[r+1][j] == numpy.inf) or (s + numlists[r+1][j] < working[r+1][j]):
                        working[r+1][j] = numlists[r+1][j] + s 

    print(working[-1][0])
