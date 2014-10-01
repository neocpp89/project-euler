#!/usr/bin/env python

# If you expand the terms of (a-1)**n + (a+1)**2
# and use the binomial theorem,
# you can see that even n results in 2 + X*a**2 + XX*a**4,
# so even n means a remainder of 2 mod a**2.
# doing the same for odd n results in 2*a*n mod a**2.
# You can find the maximum through inspection,
# if a is even, n_max = a-1, so the remainder is a**2 - 2*a
# if a is odd, n_max=(a-1)/2, so the remainder is a**2 - a.
def max_remainder_mod_asq(a):
    if a % 2 == 0:
        return (a**2 - 2*a)
    else:
        return (a**2 - a)

print sum(map(max_remainder_mod_asq, range(3,1001)))
