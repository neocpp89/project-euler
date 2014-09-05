#!/usr/bin/env python

def get_children(parent, next_list):
    return [x for x in next_list if (x / 100) == (parent % 100)]

p3n = lambda n: n * (n + 1) / 2
p4n = lambda n: n ** 2
p5n = lambda n: n * (3 * n - 1) / 2
p6n = lambda n: n * (2 * n - 1)
p7n = lambda n: n * (5 * n - 3) / 2
p8n = lambda n: n * (3 * n - 2)

trial_start = 18
trial_end = 142

trial_nums = range(trial_start, trial_end+1)

p = []
p.append([x for x in map(p3n, trial_nums) if x >= 1000 and x < 10000])
p.append([x for x in map(p4n, trial_nums) if x >= 1000 and x < 10000])
p.append([x for x in map(p5n, trial_nums) if x >= 1000 and x < 10000])
p.append([x for x in map(p6n, trial_nums) if x >= 1000 and x < 10000])
p.append([x for x in map(p7n, trial_nums) if x >= 1000 and x < 10000])
p.append([x for x in map(p8n, trial_nums) if x >= 1000 and x < 10000])
print p

maxi = len(p)
for i,pl in enumerate(p):
    n = i + 3
    pl_next = p[(i + 1) % maxi]
#    print n
#    print pl
    xform_next = map(lambda x: x / 100, pl_next)
#    print xform_next
    for num in pl:
        if (num % 100) not in xform_next:
            pl.remove(num)

for num in p[0]:
    tree = []
    
    xform_next = map(lambda x: x / 100, pl_next)
