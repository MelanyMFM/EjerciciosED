

diccionario = set()

def compuesta(palabra):
    global diccionario


    for i in range(1, len(palabra)):
        primera =palabra[:i]
        segunda = palabra[i:]
        if primera in diccionario and segunda in diccionario: return [primera, segunda]
            
    return []

while True:
    x = input()
    if x == "#": break
    else: diccionario.add(x)


compuestas = []

for i in diccionario:
    lis = compuesta(i)
    if len(lis) > 0:
        compuestas.append([i, lis[0], lis[1]])


lista_ordenada = sorted(compuestas, key=lambda x: (x[0], x[1], x[2]))

for i in lista_ordenada:
    print(f'{i[0]} = {i[1]} + {i[2]}')

