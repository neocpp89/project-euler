#!/usr/bin/env python
import math

with open('base_exp.txt') as f:
    base_exp_pairs = map(lambda line: map(int, line.split(',')), f)
    print base_exp_pairs
    
    logs = map(lambda be: math.log10(be[0]) * be[1], base_exp_pairs)
    maxl = max(logs)
    print maxl, 1+logs.index(maxl)
