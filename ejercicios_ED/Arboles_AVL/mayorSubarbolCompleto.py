from collections import deque
import sys
input = sys.stdin.read
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree:
    def __init__(self):
        self.root = None
 
    def insert(self, root, key):
        # Inserción estándar de AVL
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
     
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
 
   
        balance = self.get_balance(root)
 
      
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
 
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
 
 
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
 
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
 
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def get_height(self, node):
        if not node:
            return 0
        return node.height
 
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
 
    def subarbol(self, node):
  
        def h(n):
            if n is None:
                return 0, True, 0 
 
            izq_height, izq_completo, izq_max = h(n.left)
            der_height, der_completo, der_max = h(n.right)
 
            altura = 1 + max(izq_height, der_height)
 
            if izq_completo and der_completo and izq_height == der_height:
              
                completo = True
                max_completo = altura
            else:
               
                completo = False
                max_completo = max(izq_max, der_max)
 
            return altura, completo, max_completo
 
        _, _, max_p = h(node)
        return max_p
 
 
data = input().split()
idx = 0
while idx < len(data):
    N = int(data[idx])
    idx +=1
    if N ==0:
        break
    elements = []
    for _ in range(N):
        if idx < len(data):
            elements.append(int(data[idx]))
            idx +=1
    tree = AVLTree()
    root = None
    for elem in elements:
        root = tree.insert(root, elem)
    print(tree.subarbol(root))