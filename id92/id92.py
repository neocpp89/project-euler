#!/usr/bin/env python

def sum_sq_digits(n):
    return sum(map(lambda x: int(x)**2, list(str(n))))

goes_to_1 = set([1])
goes_to_89 = set([89])

lim = 10 ** 7

for x in range(1, 1 + lim):
    l = [x]
    while True:
        if x in goes_to_89:
            goes_to_89 |= set(l)
            break
        elif x in goes_to_1:
            goes_to_1 |= set(l)
            break
        else:
            x = sum_sq_digits(x)
            l.append(x)

print len(goes_to_89)
