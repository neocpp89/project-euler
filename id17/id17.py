#!/usr/bin/env python
import math
import sys
import string
import re

def unit_names(u):
    if u == 0:
        return 'zero'
    elif u == 1:
        return 'one'
    elif u == 2:
        return 'two'
    elif u == 3:
        return 'three'
    elif u == 4:
        return 'four'
    elif u == 5:
        return 'five'
    elif u == 6:
        return 'six'
    elif u == 7:
        return 'seven'
    elif u == 8:
        return 'eight'
    elif u == 9:
        return 'nine'
    else:
        return None

def teen_names(u):
    if (u >= 0 and u <= 9):
        return unit_names(u)
    elif u == 10:
        return 'ten'
    elif u == 11:
        return 'eleven'
    elif u == 12:
        return 'twelve'
    elif u == 13:
        return 'thirteen'
    elif u == 14:
        return 'fourteen'
    elif u == 15:
        return 'fifteen'
    elif u == 16:
        return 'sixteen'
    elif u == 17:
        return 'seventeen'
    elif u == 18:
        return 'eighteen'
    elif u == 19:
        return 'nineteen'
    else:
        return None
        
def ten_names(u):
    if u == 0:
        return 'zero'
    elif u == 1:
        return 'ten'
    elif u == 2:
        return 'twenty'
    elif u == 3:
        return 'thirty'
    elif u == 4:
        return 'forty'
    elif u == 5:
        return 'fifty'
    elif u == 6:
        return 'sixty'
    elif u == 7:
        return 'seventy'
    elif u == 8:
        return 'eighty'
    elif u == 9:
        return 'ninety'
    else:
        return None
        
def to_english(n):
    # thousands part
    th = (n / 1000) % 10
    h = (n / 100) % 10
    t = (n / 10) % 10
    u = n % 10

    if (th != 0):
        th_str = unit_names(th) + ' thousand'
    else:
        th_str = ''
        
    if (h != 0):
        h_str = unit_names(h) + ' hundred'
    else:
        h_str = ''
        
    if (t == 0):
        t_str = ''
    elif (t == 1):
        t_str = teen_names(10 + u)
    else:
        t_str = ten_names(t)
        
    if (t != 1):
        if (u != 0):
            u_str = unit_names(u)
        else:
            u_str = ''
    else:
        u_str = ''
        
    tu_str = t_str + ('-' if t_str != '' and u_str != '' else '') + u_str if (t_str != '' or u_str != '') else ''
    
    return th_str + ' ' + h_str + ((' and ') if ((th_str != '' or h_str != '') and tu_str != '') else ('')) + tu_str
    
s = 0
n = 1000
for i in xrange(1,n+1):
    s += len(to_english(i).replace(' ', '').replace('-',''))
    
print s