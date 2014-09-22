#!/usr/bin/env python

def get_children(parent, next_list):
    return [x for x in next_list if (x / 100) == (parent % 100)]

def get_upper_digits(n):
    return n / 100

def get_lower_digits(n):
    return n % 100

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
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p3n, trial_nums)))
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p4n, trial_nums)))
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p5n, trial_nums)))
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p6n, trial_nums)))
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p7n, trial_nums)))
p.append(filter(lambda x: x >= 1000 and x < 10000, map(p8n, trial_nums)))
print p

maxi = len(p)

def nn(ll=p[0], depth=0):
    if depth == maxi:
        return ll
    t = []
    for i,num in enumerate(ll):
        next_upper = filter(lambda x: get_upper_digits(x) == get_lower_digits(num), p[(depth + 1) % maxi])
        s = [num]
        s.extend(nn(next_upper, depth+1))
        t.append(s)

    return t

# tree = nn()
# print tree

s = sorted(list(set([x for ll in p for x in ll])))
print s

possible_map = [filter(lambda x: get_upper_digits(x) == get_lower_digits(y), s) for y in s]

print possible_map

def visit(nums, last):
    if (None not in nums):
        a = set(map(get_lower_digits, nums))
        b = set(map(get_upper_digits, nums))
        if (a == b and len(a) == 6):
            print nums, sum(nums)
        return
    for ps in possible_map[s.index(last)]:
        for i,ll in enumerate(p):
            if (nums[i] != None):
                continue
            if ps in ll:
                cp = list(nums)
                cp[i] = ps
                visit(cp, ps)
    return

for x in s:
    visit([None]*len(p), x)

