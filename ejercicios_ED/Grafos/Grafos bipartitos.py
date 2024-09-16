class Nodo:
    def __init__(self, id):
        self.color = None
        self.visitado = False
        self.id = id
        self.aristas = []


n, m  = input().split() #nodos, aristas
n, m = int(n), int(m)

grafo = [Nodo(i) for i in range(n)]

for _ in range(m):
    a, b = input().split(", ")
    a, b = int(a), int(b)

    grafo[a].aristas.append(grafo[b])
    grafo[b].aristas.append(grafo[a])


