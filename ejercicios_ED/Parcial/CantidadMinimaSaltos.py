#for each nodo u:
#   u.visited = false
#a.visited = true
#a.hops = 0
#q = new queue
#q.push(a)
#while (q is not empty):
#   u = q.pop()
#   for each arista (u, v):
#       if v.visited = false:
#           v.visited = true
#           v.hops = u.hops + 1
#           q.push(v)