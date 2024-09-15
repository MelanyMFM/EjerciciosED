from collections import deque



class Persona:
    def __init__(self, id):
        self.id = id
        self.amigos = None
        self.escuchoChisme = False


personas = [Persona(i) for i in range(int(input()))]

def contadorAmigo(persona):
    global personas
    cont = 0
    for i in range(len(persona.amigos)):
        if personas[i].escuchoChisme == False: cont += 1

    return cont



for j in range(len(personas)):
    temp = list(map(int, input().split()))
    if temp[0] == -1: personas[j].amigos = []
    else:
        temp = [personas[temp[i]] for i in range(len(temp))]
        personas[j].amigos = temp

empezo = 0

personas[empezo].escuchoChisme = True
q = deque()
q.append(personas[empezo])

dia = 1
contDia = len(personas[empezo].amigos)
nextDia
while len(q) > 0:
    u = q.popleft()
