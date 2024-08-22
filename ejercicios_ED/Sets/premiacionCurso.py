ej1, ej2, ej3, ej4, ej5 = set(),set(),set(),set(),set()

def agregar(id, i):
    global ej1, ej2, ej3, ej4, ej5

    if i == 1: ej1.add(id)
    elif i == 2: ej2.add(id)
    elif i == 3: ej3.add(id)
    elif i == 4: ej4.add(id)
    elif i == 5: ej5.add(id)

for i in range(1, 6):
    x = int(input())
    for _ in range(x):
        t = int(input())
        agregar(t, i)

todos = ej1&ej2&ej3&ej4&ej5

print(1000000//len(todos) if len(todos)>0 else "Nadie gana")