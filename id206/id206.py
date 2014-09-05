#!/usr/bin/env python
import math

smallest = math.sqrt(1020304050607080900L) 
largest  = math.sqrt(1930000000000000000L)

def has_form(x):
    tmp = x
    i = 10
    passed = True
    while (tmp > 0):
        if (tmp % 10 != (i % 10)):
            passed = False
            break
        tmp = tmp / 100
        i -= 1

    return passed

trial = int(math.ceil(largest)) / 10
#trial = int(math.ceil(smallest)) / 10

while not has_form(trial * trial * 100):
    trial -= 1
    #trial += 1

print trial*10
