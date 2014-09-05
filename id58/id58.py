#!/usr/bin/env python
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def spiral_diags(sidelength):
    s = sidelength
    lrc = s ** 2
    return map(lambda x: lrc - x * (s - 1), range(0,4)[::-1])

acc = [1]
total = 1
acc_prime = 0
i = 3
while True:
    total += 4
    
    diags = spiral_diags(i)
#    print diags
    acc_prime += sum(map(is_prime, diags))
    ratio = float(acc_prime) / float(total)
    if (ratio <= 0.1):
        print i
        break
    i += 2

