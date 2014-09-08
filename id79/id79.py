#!/usr/bin/env python
import itertools

def verifysequence(seq, fmls):
    for fml in fmls:
        try:
            a = seq.index(fml[0])
            b = seq.index(fml[1], a)
            c = seq.index(fml[2], b)
        except:
            return False
    return True

def verifyseq2(seqlist, fmls):
    for fml in fmls:
        d = 0
        for i in range(0, len(seqlist)):
            if (fml[d] in seqlist[i]):
                d += 1
        if (d < 3):
            return False
    return True        

def possibleseqs(f, fm, m, ml, l, places):
    seqs = []
    if places < 5:
        yield []

    for i in range (0, len(f) * len(fm) * len(ml) * len (l) * (len(m) ** (places - 4))):
        fi, fmi, mli, li = (
                i % len(f),
                (i / len(f)) % len(fm),
            )

with open('p079_keylog.txt') as f:
    attempts = list(set(map(int, f)))
    print sorted(attempts)
    
    first = map(lambda s: s/100, attempts)
    middle = map(lambda s: ((s/10) % 10), attempts)
    last = map(lambda s: s % 10, attempts)
    digits = sorted(list(set(first+middle+last)))
    print sorted(list(set(first))), sorted(list(set(last)))
    print digits

    f = list(set(first))
    fm = list(set(first + middle))
    m = digits
    ml = list(set(middle + last))
    l = list(set(last))
    

    fml = zip(first, middle, last)

    for places in range(len(digits), 1+10*len(digits)):
        for s in itertools.combinations_with_replacement(digits, places):
            for seq in itertools.permutations(s):
                if (verifysequence(list(seq), fml)):
                    print 'Possible:', list(seq)
                    exit(0)
                # else:
                   # print '!', seq
