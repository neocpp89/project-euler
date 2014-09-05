#!/usr/bin/env python
import math
def is_square(apositiveint):
  if (apositiveint == 1):
    return True
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def t(n):
    return (n * (n + 1) / 2)

def p(n):
    return (n * (3 * n - 1) / 2)

def h(n):
    return (n * (2 * n - 1))

hn_start = 143
i = hn_start
while True:
    i = i + 1
    tmp = 24 * h(i) + 1
    if is_square(tmp) == False:
        continue
    if (math.sqrt(tmp) % 6 != 5):
        continue
    print h(i), 2*i - 1, int((math.sqrt(tmp) + 1) / 6), i
    break

