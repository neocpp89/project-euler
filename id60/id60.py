#!/usr/bin/env python
import math
import itertools
import sys

# from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python
def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def aliquot(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    for i in xrange(1,lim+1):
        if n % i == 0:
            if (i == n/i):
                s += i
            else:
                s += i + n/i
            
    return (s - n)

def prime_factors(n, plist):
    a = n
    f = []
    while a not in plist:
        for p in plist:
            if a % p == 0:
                a = a / p
                f.append(p)
                break
    f.append(a)
    return f

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
#    print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

#aq = [aliquot(x) for x in xrange(0,1000001)]
#prime = [x for x in xrange(0,len(aq)) if aq[x] == 1]
prime = sundaram3(int(1e4))
filtered_primes = [p for p in prime if (p != 2 and p != 5)]
maxprime = filtered_primes[-1]
print 'done making prime list'

#candidates = []
#for i in range (1, 5):
#    print 'pass', i
#    for p in itertools.combinations(filtered_primes, 5):
#        pflag = True
#    #    print p
#        for anytwo in itertools.combinations(p, 2):
#            st = map(str, list(anytwo))
#    #        print st
#            if is_prime(int("".join(st))) == False:
#                pflag = False
#                break
#            if is_prime(int("".join(st[::-1]))) == False:
#                pflag = False
#                break
#        if pflag:
#            print p

candidates = map(lambda x: [x], filtered_primes)
for i in range (1, 5):
    new_candidates = set([])
    print 'pass', i
    num_total = len(candidates)
    for j,el in enumerate(candidates):
        for p in filtered_primes:
            pflag = True
            sp = str(p)
            sel = map(str, el)
            if ((i == 1)):
                for slel in sel:
                    if is_prime(int(slel + sp)) == False:
                        pflag = False
                        break
                    if is_prime(int(sp + slel)) == False:
                        pflag = False
                        break
            else:
                plist = pairwise.get(sp)
                if (plist == None):
                    pflag = False
                    break
                pflag = all(pairs in plist for pairs in sel)
            if pflag:
                nl = list(el)
                nl.append(p)
#                print nl
                new_candidates.add(tuple(sorted(nl)))
        print ("\r%d/%d" % (j, num_total)),
        sys.stdout.flush()
    if (i == 1):
        pairwise = {}
        for c in new_candidates:
            c = map(str, list(c))
            if (c[0] not in pairwise):
                pairwise[c[0]] = set()
            pairwise[c[0]].add(c[1])
            if (c[1] not in pairwise):
                pairwise[c[1]] = set()
            pairwise[c[1]].add(c[0])
#        print pairwise
    candidates = new_candidates
    print '\n', candidates

