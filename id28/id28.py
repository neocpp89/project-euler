#!/usr/bin/env python

N = 1001
S_tr = [(2*n + 1) ** 2 for n in xrange(0, 1+(N-1)/2)]
S_tl = [(2*n + 1) ** 2 - 2*n for n in xrange(1, 1+(N-1)/2)]
S_bl = [(2*n + 1) ** 2 - 4*n for n in xrange(1, 1+(N-1)/2)]
S_br = [(2*n + 1) ** 2 - 6*n for n in xrange(1, 1+(N-1)/2)]


print S_tr
print S_tl
print S_bl
print S_br

print sum(S_tr) + sum(S_tl) + sum(S_bl) + sum(S_br)
print 4 * sum(S_tr) - 1.5 * (N ** 2 - 1) - 3