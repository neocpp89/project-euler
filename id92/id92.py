#!/usr/bin/env python

def sum_sq_digits(n):
    return sum(map(lambda x: int(x)**2, list(str(n))))

lim = 10 ** 7

eightynines = [False]*(1+lim)
eightynines[89] = True
ones = [False]*(1+lim)
ones[1] = True

for x in range(1, 1 + lim):
    if eightynines[x] or ones[x]:
        continue

    l = [x]
    while True:
        if eightynines[x]:
            for y in l:
                eightynines[y] = True
            break
        elif ones[x]:
            for y in l:
                ones[y] = True
            break
        else:
            x = sum_sq_digits(x)
            l.append(x)

print sum([1 for x in eightynines if x]) 
