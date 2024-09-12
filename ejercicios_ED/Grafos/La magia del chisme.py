class Persona:
    def __init__(self, id):
        self.id = id
        self.amigos = None
        self.contoChisme = 0
        self.escuchoChisme = False


personas = [Persona(i) for i in range(int(input()))]


for i in range(len(personas)):
    temp = list(map(int, input().split()))
    if temp[0] == -1: temp = []
    if temp != []: 
        for j in range(len(temp)):
            personId = temp[j]
            temp[j] = personas[personId]

    personas[i].amigos = temp

casos = list(map(int, input().split(", ")))

for originoChisme in casos:
    




