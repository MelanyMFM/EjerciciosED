from collections import deque

class Persona:
    def __init__(self, id):
        self.visitado = False
        self.parientes = []
        self.id = id


for _ in range(int(input())):
    registros = {} #id:Persona

    for _ in range(int(input())):  #por número de registros

        id1, id2 = input().split()
        id1, id2 = int(id1), int(id2)

        if id1 not in registros: registros[id1] = Persona(id1)
        if id2 not in registros: registros[id2] = Persona(id2)

        registros[id1].parientes.append(registros[id2])
        registros[id2].parientes.append(registros[id1])


    c = 0
    res = 0
    fd = 0
    for i in registros:
        if registros[i].visitado == False: c += 1
        

        s = deque()
        s.append(registros[i])
        
        while len(s) > 0:
            u = s.pop()

            if u.visitado == False:
                u.visitado = True
                fd += 1
                for j in u.parientes: 
                    s.append(j)
                    

        res = max(res, fd)
        fd = 0

    print(c, res)

        

    