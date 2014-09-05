#!/usr/bin/env python
import math
import decimal
import sympy

# s = '0123'
# nums = [int(x) for x in str]
# for i in xrange()

def fast_fib(x):
    psi = (1 + math.sqrt(5)) / 2
    return (decimal.getcontext().power(decimal.Decimal(psi), x) / decimal.Decimal(math.sqrt(5)) + decimal.Decimal(0.5))

log_F_wanted = 999
psi = (1 + math.sqrt(5)) / 2
n = (math.log10(math.sqrt(5)) + log_F_wanted) / math.log10(psi)
print (math.log10(math.sqrt(5)) + log_F_wanted) / math.log10(psi)
print fast_fib(int(math.ceil(n)))