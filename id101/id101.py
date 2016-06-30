#!/usr/bin/env python

def u(n):
    return (
        1
        - n
        + (n ** 2)
        - (n ** 3)
        + (n ** 4)
        - (n ** 5)
        + (n ** 6)
        - (n ** 7)
        + (n ** 8)
        - (n ** 9)
        + (n ** 10)
    )

def backsub(U, b):
    rows = len(U)
    cols = len(U[0])
    x = [0] * rows
    for j in range(cols - 1, -1, -1):
        x[j] = b[j]
        for i in range(cols - 1, j, -1): 
            x[j] -= U[j][i] * x[i]
        x[j] /= U[j][j]
    return x

def solve(A, b):
    rows = len(A)
    cols = len(A[0])
    # print A
    for i in range(0, cols):
        g = A[i][i]
        if g == 0:
            print 'g = 0 in gaussian elimination'
        for j in range(i+1, cols):
            if A[j][i] != 0:
                f = A[j][i]
                for k in range(i, cols):
                    A[j][k] = -g * A[j][k] + f * A[i][k]
                b[j] = -g * b[j] + f * b[i]
    # print A
    # print b
    return backsub(A, b)

def make_poly(seq):
    rows = len(seq)
    cols = len(seq)
    A = []
    for i in range(0, rows):
        r = []
        for j in range(0, cols):
            r.append((i+1) ** j)
        A.append(r)
    return solve(A, seq)

def eval_poly(p, x):
    p = p[::-1]
    y = p[0]
    for c in p[1:]:
        y = (x * y + c)
    return y

bops = []
for order in range(0, 10):
    # p = make_poly(map(lambda x: x**3, range(1, order+2)))
    p = make_poly(map(u, range(1, order+2)))
    print p
    fit = 1
    while (u(fit) == eval_poly(p, fit)):
        fit += 1
    bop = eval_poly(p, fit)
    print bop
    bops.append(bop)

print sum(bops)

# A = [
#     [1,1,2,3,4,5],
#     [1,0,2,3,4,5],
#     [1,0,0,3,4,5],
#     [1,0,0,0,4,5],
#     [1,0,0,0,0,5],
#     [1,0,0,0,0,0],
#     ]
# b = [15,14,12,9,5,10]
# x = backsub(A, b)
# print x
# x = solve(A, b)
# print x

