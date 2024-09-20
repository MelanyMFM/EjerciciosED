#for each nodo u:
#   u.visited = false
#   c = 0
#   for each nodo a:
#       if a.visited = false:
#           c += 1
#   s = new stack
#   s.push(a)
#   while (s is not empty):
#       u = s.pop()
#       if u.visited = false:
#           u.visited = true
#           for each arista (u, v):
#               if v.visited = false:
#                   s.push(v)