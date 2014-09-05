#!/usr/bin/env python
import math

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

def prime_factors_no_list(n):
    lim = int(math.floor(math.sqrt(n)))
    s = 0
    pf = []
    for i in xrange(2,lim+1):
        while n % i == 0:
            pf.append(i)
            n = n / i
    if n != 1:
        pf.append(n)
    return pf
 

search = 1000000
#aq = [aliquot(x) for x in range(0,search+1)]
#prime = [x for x in range(0,len(aq)) if aq[x] == 1]

run = 0
wantrun = 4 
for n in range(100000, search+1, wantrun):
    # p = prime_factors(n, prime)
    p = prime_factors_no_list(n)
    if len(set(p)) == wantrun:
        print 'Has 4 distinct prime factors: ', n, p
        run = 1
        s = 1
        # while (len(set(prime_factors(n-s, prime))) == wantrun):
        while (len(set(prime_factors_no_list(n-s))) == wantrun):
            run += 1
            s += 1
        i = 1
        # while (len(set(prime_factors(n+i, prime))) == wantrun):
        while (len(set(prime_factors_no_list(n+i))) == wantrun):
            run += 1
            i += 1
 
        if (run >= wantrun):
            print 'First number:', n-s+1
            break
    else:
        run = 0
