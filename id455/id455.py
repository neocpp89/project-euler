# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:58:35 2014

@author: sdunatunga
"""

import math

def trailfunc(n,x):
    if (x == math.pow(n,x,1e9)):
        r = x
    else:
        r = 0
    return r
    
m = max(map(lambda x: trailfunc(4,x), range(0,int(1e9+1))))

print m