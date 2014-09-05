#!/usr/bin/env python
import itertools

digits = range(1,10)
sdigits = map(str, digits)

for i in range(1,5):
	for p in itertools.permutations(digits, i):
		z = [9]
		z.extend(list(p)) 
		z = int("".join(map(str, z)))
	#	print z
		q = map(lambda x: x*z, range(1,5))
		s = "".join(map(str, q))[0:9]
		if (sorted(s) == sdigits):
			print 'pandigital', s
		#else:
		#	print s


