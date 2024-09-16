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
for _ in range(int(input())):
    dict = {}
    ya  = set()

    a, b = input().split()
    a, b = list(a), list(b)
    a[1], b[1], a[0], b[0] = int(a[1])-1, int(b[1])-1, letra(a[0]), letra(b[0])
    a, b = tuple(a), tuple(b)


    s = deque()
    s.append(a)
    dict[a] = 0
    encontrado = False
    ya.add(a)

    while len(s) > 0 and not encontrado:
        u = s.popleft()

        for i in saltos(u[0], u[1]):
            if i not in ya:
                dict[i] = dict[u] + 1

                ya.add(i)
                s.append(i)
                if i == b:
                    encontrado = True
                    break

                


    print(dict[b])

