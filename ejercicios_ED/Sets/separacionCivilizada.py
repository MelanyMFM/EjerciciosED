fernando, gustavo = set(), set()

def agregar(L, id):
    global fernando, gustavo

    if L == "F":
        if id not in gustavo:
            fernando.add(id)
        else:
            if id%2 == 0:
                fernando.add(id)
                gustavo.remove(id)

    else:
        if id not in fernando:
            gustavo.add(id)
        else:
            if id%2 != 0:
                gustavo.add(id)
                fernando.remove(id)

while True:
    x = input()
    if x == "0": break

    x = x.split()
    
    agregar(x[1], int(x[0]))


print(len(fernando), len(gustavo))
