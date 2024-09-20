from collections import deque

class Nodo:
    def __init__(self, id):
        self.color = None
        self.visitado = False
        self.id = id
        self.aristas = []


def contrario(color):
    return "dabadaba" if color == "dubidubi" else "dubidubi"

for _ in range(int(input())):
    n, m  = input().split() #nodos, aristas
    n, m = int(n), int(m)

    grafo = [Nodo(i) for i in range(1, n+1)]
    grafo.insert(0, None)

    for _ in range(m):
        a, b = input().split(", ")
        a, b = int(a), int(b)

        grafo[a].aristas.append(grafo[b])
        grafo[b].aristas.append(grafo[a])

    bipartito = True
    siga = True

    for i in grafo:
        if i == None: continue
        if i.visitado == True: continue 

        q = deque()
        i.visitado = True
        i.color = "dubidubi"
        q.append(i)

        while len(q) > 0 and siga:
            u = q.popleft()

            for j in u.aristas:

                if j.visitado == False:
                    j.visitado = True
                    j.color = contrario(u.color)
                    q.append(j)

                else:
                    if j.color != contrario(u.color): 
                        bipartito = False
                        siga = False


    print("bipartito" if bipartito else "no bipartito")
