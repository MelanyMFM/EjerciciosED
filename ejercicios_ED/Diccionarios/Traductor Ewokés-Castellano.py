dict = {}

for _ in range(int(input())):
    x = input().split()
    dict[x[0]] = x[1]


while True:
    x = input()
    if x == "#": break
    if x in dict: 
        print(dict[x]) 
    else: 
        print("Entrada no encontrada")

