from collections import deque
from math import floor

res = deque()

M = int(input()) #premio total

sms = {} #numero sms - cantidad
ganadores = set()
numbers = set()


def won(numero):
    global ganadores, sms, M, res
    G = len(ganadores)
    C = sms[numero]

    premio = floor(M / (G*C))
    res.append([numero, premio])


def agregar(palabra, numero):
    global sms, winners, ganadores, numbers
    if palabra == "sms":
        if int(numero) in numbers: sms[int(numero)] += 1
        else: 
            sms[int(numero)] = 1
            numbers.add(int(numero))
        if int(numero) in ganadores: 
        
            won(int(numero))

    elif palabra == "winner": 
   
        ganadores.add(int(numero))


while True:
    x = input()
    if x == "end": break
    else:
        x = x.split()
        agregar(x[0], x[1])


if len(res) == 0: print(0)
else:
    for i in res:
        print(i[0], i[-1])

