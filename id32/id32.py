#!/usr/bin/env python

def has_digits_in_list(a,b):
    s = map(str, b)
    s.sort()
    s = reduce(lambda x,y: x+y, s)
    i = [ch for ch in str(a)]
    i.sort()
    i = reduce(lambda x,y: x+y, i)
    if (s == i):
        return True
    else:
        return False


def do_pandigital_mult(digits, ll, lr, nl, nr):
    if (ll > 0):
        for i,d in enumerate(digits):
            do_pandigital_mult(digits[:i] + digits[i+1:], ll-1, lr, nl*10+d, nr)
    elif (lr > 0):
        for i,d in enumerate(digits):
            do_pandigital_mult(digits[:i] + digits[i+1:], ll, lr-1, nl, nr*10+d)
    else:
        m = (nl * nr)
        print has_digits_in_list(m, digits), m, nl, nr

#def do14mult(digits, l1, l4, n1, n4):
#    if (l1 > 0):
#        for i,d in enumerate(digits):
#            do14mult(digits[:i] + digits[i+1:], l1-1, l4, n1*10+d, n4)
#    elif (l4 > 0):
#        for i,d in enumerate(digits):
#            do14mult(digits[:i] + digits[i+1:], l1, l4-1, n1, n4*10+d)
#    else:
#        m = (n1 * n4)
#        print has_digits_in_list(m, digits), m, n1, n4

digits = [1,2,3,4,5,6,7,8,9]
#print has_digits_in_list(4221, [2,1,4])
do_pandigital_mult(digits, 1, 4, 0, 0)
do_pandigital_mult(digits, 2, 3, 0, 0)

