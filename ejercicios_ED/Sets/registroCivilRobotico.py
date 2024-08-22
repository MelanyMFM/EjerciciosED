poblacion = set()

def new(x, y):
    global poblacion

    if x in poblacion and y in poblacion:
        hijo = x+y
        while True:
            if hijo not in poblacion:
                poblacion.add(hijo)
                break
            hijo += 1

def search(x):
    global poblacion

    print("existe" if x in poblacion else "no existe")


for i in range(1, int(input())+1):
    poblacion.add(i)

while True:
    x = input()
    if x == "#": break
    x = x.split()

    if x[0] == "new": new(int(x[1]), int(x[2]))
    else: search(int(x[1]))
