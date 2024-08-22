poblacion = set()
muertos = set()

def agregar(L, id):
    global poblacion
    global muertos

    if L == "B":
        if id not in poblacion and id not in muertos: poblacion.add(id)

    if L == "D":
        if id in poblacion: 
            poblacion.remove(id)
            muertos.add(id)

    if L == "R":
        if id not in poblacion and id in muertos: 
            poblacion.add(id)
            muertos.remove(id)

while True:
    x = input()
    if x == "E": break

    x = x.split()
    agregar(x[0], int(x[1]))

print(len(poblacion))