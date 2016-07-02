#!/usr/bin/env python
import csv

with open('./p107_network.txt', 'r') as f:
    reader = csv.reader(f)
    graph = []
    for line in reader:
        adj_list = []
        for i,tok in enumerate(line):
            if (tok == '-'):
                print 'ignore'
            else:
                adj_list.append((i, int(tok)))
        graph.append(adj_list)

    print graph

node_states = [0] * len(graph)
node_weights = [10000000000000000] * len(graph)

s = set([0])

msw = 0
while len(s) != len(graph):
    mw = 1000000000000
    mi = 0
    for current in s:
        for i, w in graph[current]:
            if w < mw and i not in s:
                mi = i
                mw = w
    s.add(mi)
    msw += mw

ow = 0
for i, li in enumerate(graph):
    for j, w in li:
        if i < j:
            ow += w

print s, msw, ow, ow - msw
