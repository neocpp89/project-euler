#!/usr/bin/env python
import math

def sequence_sum(start, n_terms, increment):
    return n_terms*start + increment*(n_terms)*(n_terms+1)/2

n = 999
print sequence_sum(0, math.floor(n/3), 3) + sequence_sum(0, math.floor(n/5), 5) - sequence_sum(0, math.floor(n/15), 15)
 