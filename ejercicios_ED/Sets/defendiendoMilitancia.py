pdd, pdi, pdc = set(), set(), set()

def vota(partido, id):
    global pdd, pdi, pdc

    if partido == "pdd": pdd.add(id)
    elif partido == "pdi": pdi.add(id)
    elif partido == "pdc": pdc.add(id)


while True:
    x = input()
    if x == "#": break
    x = x.split()
    vota(x[1], int(x[0]))

unPartido = (pdd - pdi - pdc) | (pdi - pdd - pdc) | (pdc - pdd - pdi)
tresPartidos = pdd & pdi & pdc
dosPartidos = (pdd & pdi - tresPartidos) | (pdi & pdc - tresPartidos) | (pdd & pdc - tresPartidos)


print(len(unPartido), len(dosPartidos), len(tresPartidos))
