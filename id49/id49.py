#!/usr/bin/env python
import math

def hashprime(p):
    return int(strcat(sorted(str(p))))

def strcat(li):
    s = ''
    for l in li:
        s = s + l
    return s

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

alist = map(aliquot, xrange(1000, 10000))
primes = [i+1000 for i,a in enumerate(alist) if a == 1]

#print primes

#sprimes = map(strcat,map(sorted,map(str, primes)))
#print(sprimes)

#hashed_primes = map(int, sprimes);

hashed_primes = map(hashprime, primes)

possible = {}

for p in set(hashed_primes):
#    print '['
    possible[str(p)] = []
    for i,pt in enumerate(hashed_primes):
        if (p == pt):
            possible[str(p)].append(primes[i])
#            print '\t', primes[i]
#    print ']'

#print possible

noprint = True

while noprint:
    for key in possible.keys():
        first = possible[key][0]
        if len(possible[key]) >= 3:
            delta = possible[key][1] - first
            if (first + delta*2) in possible[key]:
                print first, first+delta, first+2*delta
                noprint = False
            else:
                possible[key].remove(first)

#for i,p in enumerate(hashed_primes):
#    for pt in hashed_primes:
#        if (p == pt):
#            possible[i] = possible[i] + 1

#print possible

#for i,p in enumerate(possible):
#    if (p) >= 9:
#        print primes[i]

