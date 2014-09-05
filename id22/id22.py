#!/usr/bin/env python
import string

def score(str, smap):
    s = 0
    for c in str:
        s += smap[c]
    return s
    
def make_scoremap():
    uc = string.ascii_uppercase
    scoremap = {}
    for i in xrange(0, len(uc)):
        scoremap[uc[i]] = (i + 1)
    return scoremap
    
with open('names.txt', 'r') as file:
    smap = make_scoremap()
    namelist = []
    for line in file:
        for name in line.replace('"', '').split(','):
            namelist.append(name)
    namelist.sort()
    
    total = 0
    for i in xrange(0, len(namelist)):
        total += (i + 1)*score(namelist[i], smap)
 
    print total