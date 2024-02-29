from collections import deque
casos = int(input())
res = []
def mover(f1, f2):
  global A, B,C
  if f1 == "A":
    f1 = A
  elif f1 == "B":
    f1 = B
  elif f1== "C":
    f1 = C
  if f2 == "A":
    f2 = A
  elif f2 == "B":
    f2 = B
  elif f2 == "C":
    f2= C
    
  if (not f1):
    return "invalido"
  elif f2:
    if (f1[-1] > f2[-1]):
      return "invalido"
    else:
      x = f1.pop()
      f2.append(x)
  else:
    x = f1.pop()
    f2.append(x)
   
 
A = deque()
B = deque()
C = deque()

discos = int(input())
for i in range(discos, 0, -1):
  A.append(i)
  
while casos > 0:
  x = input()
  if x == "X X":
    res.append(C)
    casos -= 1
    B = deque()
    C = deque() 
    A = deque()
    for i in range(discos, 0, -1):
      A.append(i)
    
    break
    
  else:
    x = x.split()
    res = mover(x[0], x[1])
    if res == "invalido":
      res.append("secuencia invalida")
      break

print(res)
