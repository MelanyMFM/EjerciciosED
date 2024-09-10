from collections import deque

diccionario = set()

def compuesta(palabra):
    global diccionario
    combinaciones = deque()

    for i in range(1, len(palabra)):
        primera =palabra[:i]
        segunda = palabra[i:]
        if primera in diccionario and segunda in diccionario: combinaciones.append([primera, segunda])
            
    return combinaciones

while True:
    x = input()
    if x == "#": break
    else: diccionario.add(x)


compuestas = []

for i in diccionario:
    lis = compuesta(i)
    if len(lis) > 0:

        for j in lis: compuestas.append([i, j[0], j[1]])



lista_ordenada = sorted(compuestas, key=lambda x: (x[0], x[1], x[2]))

for i in lista_ordenada:
    print(f'{i[0]} = {i[1]} + {i[2]}')

