class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    dict = {}
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key, 0)
        

    def _insertRecursively(self, root, key, x):
        
        if root is None:
            self.dict[key] = x
            return Node(key)
        
        if key < root.key:
            
            root.left = self._insertRecursively(root.left, key, x+1)
        elif key > root.key:
            
            root.right = self._insertRecursively(root.right, key, x+1)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def derecha(self):
        elements = []
        self._derecharecur(self.root, elements)
        return elements

    def _derecharecur(self, root, elements):
        if root:
            self._derecharecur(root.right, elements)
            elements.append(root.key)
            self._derecharecur(root.left, elements)
    

for _ in range(int(input( ))):
               
    tree = BinarySearchTree()
    x = list(map(int, input().split()))
    for k in x:
        
        if k == -1:
            break
        else:
            tree.insert(k)

    for i in tree.derecha():
        print(f'{"    "*tree.dict[i]}{i}')

    print()
        
