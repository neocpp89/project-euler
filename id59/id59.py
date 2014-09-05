#!/usr/bin/env python
from curses.ascii import isprint

def print_mode(thelist):
  counts = {}
  for item in thelist:
    counts [item] = counts.get (item, 0) + 1
  maxcount = 0
  maxitem = None
  for k, v in counts.items ():
    if v > maxcount:
      maxitem = k
      maxcount = v
  if maxcount == 1:
    print "All values only appear once"
    return 'o'
  elif counts.values().count (maxcount) > 1:
    print "List has multiple modes"
    return 'e'
  else:
    #print "Mode of list:", maxitem
    return maxitem

lcase = range(ord('a'), ord('z')+1)
print map(chr, lcase)

inums = []
with open('cipher1.txt', 'r') as f:
    for line in f:
        snums = line.split(',')
        inums.extend(map(int, snums))
        print inums

for key1 in lcase:
    for key2 in lcase:
        for key3 in lcase:
            xorkey = [key1, key2, key3]
            newstring = []
            for i,inum in enumerate(inums):
                newstring.append(chr(inum ^ xorkey[i % 3]))
#            mode = print_mode(newstring)
#            if (mode == 'e'):
            printable = map(lambda x: isprint(x) or (x == '\n'), newstring)
            if (all(printable)):
                mode = print_mode(newstring) 
                if (mode == 'e' or mode == ' ' or mode == 't' or mode == 'a'):
                    print map(chr,xorkey), ''.join(newstring)
                    print 'Sum:', sum(map(ord, newstring))
