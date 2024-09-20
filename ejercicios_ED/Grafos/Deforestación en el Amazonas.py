from collections import deque
for _ in range(int(input())):
    a, b = input().split()  #rows - columnas
    a, b = int(a), int(b)

    def vecinos(i, j):
        global a, b
        coords = deque()
        if j != 0:  coords.append((i, j-1))

        if i != 0: coords.append((i-1, j))

        if j != b-1: coords.append((i, j+1))

        if i != a-1: coords.append((i+1, j))

        return coords



    amazonas = [ list(input()) for _ in range(a)]

    majino = 0

    for i in range(a):
        for j in range(b):

            if amazonas[i][j] == "X":
                s = deque()
                s.append((i, j))
                cont = 0

                while len(s) > 0:
                    u = s.pop()
                    if amazonas[u[0]][u[1]] == "X":
                        amazonas[u[0]][u[1]] = "ya"
                        cont += 1

                        for kk in vecinos(u[0], u[1]):
                            if amazonas[kk[0]][kk[1]] == "X":
                                s.append(kk)

                majino = max(majino, cont)

    print(majino)