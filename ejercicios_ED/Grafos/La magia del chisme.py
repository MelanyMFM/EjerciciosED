from collections import deque

class Persona:
    def __init__(self, id):
        self.id = id
        self.amigos = None
        self.conto_chisme = 0
        self.escucho_chisme = False
        self.dia = 0
        self.segunda = False


personas = [Persona(i) for i in range(int(input()))]



for i in range(len(personas)):
    temp = list(map(int, input().split()))
    if temp[0] == -1: temp = []
    if temp != []: 
        for j in range(len(temp)):
            personId = temp[j]
            temp[j] = personas[personId]

    personas[i].amigos = temp



popo = list(map(int, input().split(", ")))
for kk in popo:
    
    for ola in personas:
        ola.segunda = False
        ola.escucho_chisme = False

    originoChisme = kk
    q = deque()
    q.append(personas[originoChisme])
    personas[originoChisme].escucho_chisme = True


    while len(q) > 0:

        u = q.popleft()

        for v in u.amigos:
            if v.escucho_chisme == False:
                v.escucho_chisme = True
                v.dia = u.dia + 1
                q.append(v)

    dias = {}
    q = deque()
    q.append(personas[originoChisme])
    personas[originoChisme].segunda = True

    while len(q) > 0:
        u = q.popleft()

        for v in u.amigos:
            if v.segunda == False:
                v.segunda = True

                if v.dia not in dias: dias[v.dia] = 1
                else: dias[v.dia] += 1
                q.append(v)


    max = 0
    cant = 0
    for i in dias:
        if cant < dias[i]:
            cant = dias[i]
            max = i

    if max != 0 and cant != 0: print(max, cant)
    else: print(0)

