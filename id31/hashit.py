#!/usr/bin/env python

def hashit(c, v):
    s = '';
    for i,ch in enumerate (c):
        s = s + str(v[i]) + ch
    return s

with open('list.txt') as f:
    for line in f:
        print hashit()
