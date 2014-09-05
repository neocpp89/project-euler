#!/usr/bin/env python

s = set()

def num_combos(val, vlist):
    if val == 0:
        return 1
    if (val < 0) or (not vlist and val > 0):
        return 0
    return num_combos(val, vlist[:-1]) + num_combos(val - vlist[-1], vlist)

#def hashit(c, v):
#    s = '';
#    for i,ch in enumerate (c):
#        s = s + str(v[i]) + ch
#    return s

#def print_combo_lines_r(clist, vlist, want, prepend):
#    if (want == 0):
#        if prepend[0] < 25:
#            print prepend
#        s.add(hashit(clist, prepend))
#        return

#    if (want < 0):
#        return

#    for i,v in enumerate(vlist):
#        prepend[i] = prepend[i] + 1
#        print_combo_lines_r(clist, vlist, want - v, prepend)
#        prepend[i] = prepend[i] - 1 

#    return

#def print_combo_lines(clist, vlist, want):
#    print_combo_lines_r(clist, vlist, want, [0 for x in xrange(0, len(vlist))])
#    return

#clist = ['p', 'n', 'd', 'q', 'h', '$']
#vlist = [1,5,10,25,50,100]

clist = ['p', 't', 'n', 'd', 'q', 'h', '$', '*']
vlist = [1,2,5,10,20,50,100,200]

#clist = ['n','d','q']
#vlist = [5,10,25]

#print_combo_lines(clist, vlist, 200)
#print s
#print len(s)

print num_combos(200, vlist)


