from collections import deque

class Persona():
    def __init__(self, id):
        self.id = id
        self.numPaulina = None
        self.bailado = []
        self.visitado = False


casos = int(input())
for p in range(casos):
    x = list(map(int, input().split(", ")))
    personas = [Persona(i) for i in range(x[0])]
    personas[0].numPaulina = 0
    
    for i in range(x[1]):
        y = list(map(int, input().split()))
        personas[y[0]].bailado.append(personas[y[1]])
        personas[y[1]].bailado.append(personas[y[0]])

    q = deque()  #Recorrido BFS
    personas[0].visitado = True
    q.append(personas[0])
    while len(q) > 0:
        u = q.popleft()
        for v in u.bailado:
            if v.visitado == False:
                v.visitado = True
                v.numPaulina = u.numPaulina + 1
                q.append(v)


    print(f'fiesta {p+1}:')

    for i in range(1, len(personas)):
        mrBeast = personas[i].numPaulina if personas[i].numPaulina != None else "INF"

        print(personas[i].id, mrBeast)

    if i+1 != casos: print()
   

