from collections import deque

def saltos(i, j):
    cheval = deque()
    if i-2 >= 0:
        if j-1 >= 0: cheval.append((i-2, j-1))
        if j+1 <= 7: cheval.append((i-2, j+1))

    if i-1 >= 0:
        if j-2 >= 0: cheval.append((i-1, j-2))
        if j+2 <= 7: cheval.append((i-1, j+2))

    if i+1 <= 7: 
        if j-2 >= 0: cheval.append((i+1, j-2))
        if j+2 <= 7: cheval.append((i+1, j+2))

    if i+2 <= 7:
        if j-1 >= 0: cheval.append((i+2, j-1))
        if j+1 <= 7: cheval.append((i+2, j+1))

    return cheval


letra = lambda x: ord(x) - 65

a, b = input().split()
a, b = list(a), list(b)
a[1], b[1] = int(a[1]), int(b[1])

