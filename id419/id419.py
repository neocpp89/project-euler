#!/usr/bin/env python
import numpy as np

cosmological_table = [
    ('', [0]),
    ('1112', [63]),
    ('1112133', [64, 62]),
    ('111213322112', [65]),
    ('111213322113', [66]),
    ('1113', [68]),
    ('11131', [69]),
    ('111311222112', [84, 55]),
    ('111312', [70]),
    ('11131221', [71]),
    ('1113122112', [76]),
    ('1113122113', [77]),
    ('11131221131112', [82]),
    ('111312211312', [78]),
    ('11131221131211', [79]),
    ('111312211312113211', [80]),
    ('111312211312113221133211322112211213322112', [81, 29, 91]),
    ('111312211312113221133211322112211213322113', [81, 29, 90]),
    ('11131221131211322113322112', [81, 30]),
    ('11131221133112', [75, 29, 92]),
    ('1113122113322113111221131221', [75, 32]),
    ('11131221222112', [72]),
    ('111312212221121123222112', [73]),
    ('111312212221121123222113', [74]),
    ('11132', [83]),
    ('1113222', [86]),
    ('1113222112', [87]),
    ('1113222113', [88]),
    ('11133112', [89, 92]),
    ('12', [1]),
    ('123222112', [3]),
    ('123222113', [4]),
    ('12322211331222113112211', [2, 61, 29, 85]),
    ('13', [5]),
    ('131112', [28]),
    ('13112221133211322112211213322112', [24, 33, 61, 29, 91]),
    ('13112221133211322112211213322113', [24, 33, 61, 29, 90]),
    ('13122112', [7]),
    ('132', [8]),
    ('13211', [9]),
    ('132112', [10]),
    ('1321122112', [21]),
    ('132112211213322112', [22]),
    ('132112211213322113', [23]),
    ('132113', [11]),
    ('1321131112', [19]),
    ('13211312', [12]),
    ('1321132', [13]),
    ('13211321', [14]),
    ('132113212221', [15]),
    ('13211321222113222112', [18]),
    ('1321132122211322212221121123222112', [16]),
    ('1321132122211322212221121123222113', [17]),
    ('13211322211312113211', [20]),
    ('1321133112', [6, 61, 29, 92]),
    ('1322112', [26]),
    ('1322113', [27]),
    ('13221133112', [25, 29, 92]),
    ('1322113312211', [25, 29, 67]),
    ('132211331222113112211', [25, 29, 85]),
    ('13221133122211332', [25, 29, 68, 61, 29, 89]),
    ('22', [61]),
    ('3', [33]),
    ('3112', [40]),
    ('3112112', [41]),
    ('31121123222112', [42]),
    ('31121123222113', [43]),
    ('3112221', [38, 39]),
    ('3113', [44]),
    ('311311', [48]),
    ('31131112', [54]),
    ('3113112211', [49]),
    ('3113112211322112', [50]),
    ('3113112211322112211213322112', [51]),
    ('3113112211322112211213322113', [52]),
    ('311311222', [47, 38]),
    ('311311222112', [47, 55]),
    ('311311222113', [47, 56]),
    ('3113112221131112', [47, 57]),
    ('311311222113111221', [47, 58]),
    ('311311222113111221131221', [47, 59]),
    ('31131122211311122113222', [47, 60]),
    ('3113112221133112', [47, 33, 61, 29, 92]),
    ('311312', [45]),
    ('31132', [46]),
    ('311322113212221', [53]),
    ('311332', [38, 29, 89]),
    ('3113322112', [38, 30]),
    ('3113322113', [38, 31]),
    ('312', [34]),
    ('312211322212221121123222113', [36]),
    ('312211322212221121123222112', [35]),
    ('32112', [37])
]

def create_transition_matrix():
    T = []
    for x in cosmological_table:
        r = [0] * len(cosmological_table)
        for l in x[1]:
            r[l] += 1
        T.append(r)
    # print T
    # print zip(*T)
    return zip(*T) # transpose the array


def las(n):
    s = str(n)
    current = s[0]
    rep = 1
    buf = []
    for c in s[1:]:
        if c == current:
            rep += 1
        else:
            buf.append(str(rep)+current)
            current = c
            rep = 1

    buf.append(str(rep)+current)
    return int("".join(buf))

def getabc(n):
    s = str(n)
    n = [0] * 10
    for c in s:
        n[int(c)] += 1
    return (n[1], n[2], n[3])

T = create_transition_matrix()
# T = np.array(T).T
# print T

# v8 = np.array([0]*93)
# v8[24] = 1
# v8[39] = 1

def _bits_of_n(n):
    bits = []
    while n:
        bits.append(n % 2)
        n /= 2
    return bits

def mm(A, B):
    C = []

    rA = len(A)
    rB = len(A[0])
    cA = rB
    cB = len(B[0])

    for i in range(0, rA):
        C.append([0] * cB)

    for i in range(0, rA):
        for j in range(0, cB):
            for k in range(0, rB):
                C[i][j] += A[i][k] * B[k][j]

    return C

def mmm(A, B, m):
    C = mm(A, B)
    rC = len(C)
    cC = len(C[0])
    for i in range(0, rC):
        for j in range(0, cC):
            C[i][j] = C[i][j] % m
    return C


#def modexp_lr(A, b, n):
#    r = np.identity(A.shape[0])
#    for bit in reversed(_bits_of_n(b)):
#        r = np.dot(r, r)
#        if bit == 1:
#            r = np.dot(r, A)
#        for x in np.nditer(r, op_flags=['readwrite']):
#            x[...] = x % n
#    return r

def modexp_lr(A, b, n):
    r = None
    for bit in reversed(_bits_of_n(b)):
        if r is not None:
            r = mmm(r, r, n)
        if bit == 1:
            if r is None:
                r = A
            else:
                r = mmm(r, A, n)
    return r

m = 2 ** 30
n = 10 ** 12
# m = 1024
# n = 43
T = modexp_lr(T, n - 8, m)

# print v8
# v = np.dot(T, v8)
# v40 = map(int, list(v40))
# v = list(v)

T = zip(*T) # transpose
v = [0]*len(T)
for i, e in enumerate(T[24]):
    v[i] = (T[24][i] + T[39][i]) % m


a, b, c = 0, 0, 0
for i, x in enumerate(v):
    s = cosmological_table[i][0]
    aa, bb, cc = getabc(s)
    a += aa * x
    b += bb * x
    c += cc * x

a, b, c = map(lambda x: x % m, (a, b, c))
print a, b, c

'''
l = 1
for x in range(1, n):
    l = las(l)
    # print getabc(l)
    aa, bb, cc = map(lambda x: x % m, getabc(l))
    if (x == n - 1):
        print aa, bb, cc
        #print aa, a
        #print bb, b
        #print cc, c
'''