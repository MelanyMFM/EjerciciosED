from collections import deque

class Persona:
    def __init__(self, id):
        self.id = id
        self.amigos = None
        self.conto_chisme = 0
        self.escucho_chisme = False


personas = [Persona(i) for i in range(int(input()))]


def amigos_no(persona):
    global personas
    cont = 0
    for i in range(len(persona.amigos)):
        if personas[persona.amigos[i]].escucho_chisme == False: cont += 1

    return cont


for i in range(len(personas)):
    temp = list(map(int, input().split()))
    if temp[0] == -1: temp = []
    if temp != []: 
        for j in range(len(temp)):
            personId = temp[j]
            temp[j] = personas[personId]

    personas[i].amigos = temp

originoChisme = 0
q = deque()
q.append(personas[originoChisme])
personas[originoChisme].escucho_chisme = True
contDia, contNextDia = 1, 0

while len(q) > 0:

    u = q.popleft()

    for v in u.amigos:
        if v.escucho_chisme == False:
            v.escucho_chisme = True
            q.append(v)


