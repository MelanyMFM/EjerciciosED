felipe, vanesa = set(), set()

def agregar(l,n):
    global felipe
    global vanesa
    felipe.add(n) if l == "F" else vanesa.add(n)


while True:
    x = input()
    if x == "#": break
    x = x.split()
    agregar(x[0], int(x[1]))

print(len(felipe), len(vanesa), len(felipe.union(vanesa)))
