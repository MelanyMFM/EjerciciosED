ya_voto = {}  #quien - por quien 
votos = {}  #por quien - cuantos
anulados = set()

def vota(quien, por):
    global ya_voto, votos,aulados

    if quien in ya_voto: 
        if quien in anulados: return
        votos[ya_voto[quien]] -= 1
        anulados.add(quien)

    else:
        ya_voto[quien] = por
        if por in votos: votos[por] += 1
        else: votos[por] = 1


while True:
    x = list(map(int, input().split()))
    

    if x[0] == 0 and x[1] == 0: break
    else:
        vota(x[0], x[1])

resultado = [(candidato, votos[candidato]) for candidato in votos if votos[candidato] > 0]
resultado.sort(key=lambda x: (-x[1], -x[0]))

for candidato, total_votos in resultado:
    print(candidato, total_votos)