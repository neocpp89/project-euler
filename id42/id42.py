#!/usr/bin/env python

def wordvalue(s):
    n = 0;
    for c in s:
        n += ord(c) - ord('A') + 1
    return n

with open('words.txt', 'r') as f:
    for line in f:
        words = line.replace('"', '').split(',')

print words
score = map(wordvalue, words)
print score

triangle_nums = [(n*n + n)/2 for n in xrange(1,20)]
print triangle_nums

total = 0
for t in triangle_nums:
    for s in score:
        if t == s:
            total += 1

print total

