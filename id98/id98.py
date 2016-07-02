#!/usr/bin/env python

def mapping(n, w):
    sn = str(n)
    used = [False]*10
    if len(sn) == len(w):
        m = {}
        for i,c in enumerate(w):
            if c in m:
                if (m[c] != sn[i]) or used[int(sn[i])]:
                    return None
            else:
                if used[int(sn[i])]:
                    return None
                m[c] = sn[i]
                used[int(sn[i])] = True
        return m
    return None

def unmapping(m, w):
    return int("".join(map(lambda c: m[c], w)))

with open('words.txt') as f:
    words = map(lambda row: map(lambda word: word.translate(None, '\n"'), row.split(',')), f)
    words = words[0]
    print words

    anagrams = {}
    for w in words:
        sw = tuple(sorted(w))
        if sw in anagrams:
            anagrams[sw].append(w)
        else:
            anagrams[sw] = [w]

    anagrams = [anagrams[key] for key in anagrams if len(anagrams[key]) > 1]
    # print anagrams

    """
    for key in anagrams:
        if (len(anagrams[key]) > 1):
            print anagrams[key]
    """

    la = {}
    for s in anagrams:
        ls = len(s[0])
        if ls in la:
            la[ls].append(s)
        else:
            la[ls] = [s]
    print la

    ma = max(la.keys())

    squares = map(lambda x: x ** 2, range(1000000))
    asquares = {}
    for s in squares:
        ss = tuple(sorted(str(s)))
        if len(ss) > ma:
            continue
        if ss in asquares:
            asquares[ss].append(s)
        else:
            asquares[ss] = [s]
    asquares = [asquares[x] for x in asquares if len(asquares[x]) > 1]
    # print asquares
    """
    ls = {}
    for s in squares:
        lss = len(str(s))
        if lss > ma:
            continue
        if lss in ls:
            ls[lss].append(s)
        else:
            ls[lss] = [s]
    """
    # print ls

    for ag in anagrams:
        f = ag[0]
        g = ag[1]
        for l in asquares:
            for x in l:
                m = mapping(x, f)
                if (m != None):
                    other = unmapping(m, g)
                    if (other in l):
                        print x, other, f, g
