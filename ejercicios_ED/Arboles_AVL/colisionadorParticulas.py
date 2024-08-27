from collections import deque

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))

        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def delete(self, key):
        self.size -= self.search(key)
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._getMin(root.right)
            root.key = temp
            root.right = self._deleteRecursively(root.right, temp)
        if root is None:
            return root

        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        balanceFactor = self._getNodeBalance(root)

        if balanceFactor > 1:
            if self._getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self._getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height

    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)

    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)

    def _getMax(self, root):
        if root is None:
            return None
        elif root.right is None:
            return root.key
        return self._getMax(root.right)

    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def posOrder(self):
        elements = []
        self._posOrderRecursively(self.root, elements)
        return elements

    def _posOrderRecursively(self, root, elements):
        if root:
            self._posOrderRecursively(root.left, elements)
            self._posOrderRecursively(root.right, elements)
            elements.append(root.key)

    def popMin(self):
        if self.size == 0:
            return None
        else:
            key = self._getMin(self.root)
            self.delete(key)
            return key
    
    def leafNodesLastLevel(self):
        self.leafsll = 0
        self.maxh = self._getNodeHeight(self.root)
        self._leafNodesLastLevelRecursively(self.root, 1)
        return self.leafsll

    def _leafNodesLastLevelRecursively(self, root, height):
        if not root:
            return
        if not root.left and not root.right and (height == self.maxh):
            self.leafsll += 1
        self._leafNodesLastLevelRecursively(root.left, height + 1)
        self._leafNodesLastLevelRecursively(root.right, height + 1)

    def rings(self):
        self.ring = ""
        self.bfs = deque([self.root])

        while self.bfs:
            act = self.bfs.popleft()
            if act.left and act.right:
                self.ring +="2."
                self.bfs.append(act.left)
                self.bfs.append(act.right)
            elif act.left and not act.right:
                self.ring += "-1."
                self.bfs.append(act.left)
            elif not act.left and act.right:
                self.ring += "1."
                self.bfs.append(act.right)
            else:
                self.ring += "0."
        
        self.ring = self.ring[:-1]
        return self.ring
    
    def printTree(self):
        self.lines = []
        self._printTreeRecursively(self.root)
        return self.lines

    def _printTreeRecursively(self, root, level=0):
        if not root:
            return
        else:
            self._printTreeRecursively(root.right, level + 1)
            self.lines.append("	"*level + str(root.key))
            self._printTreeRecursively(root.left, level + 1)
    
    def particles(self):
        while self.size > 1:
            peq = self._getMin(self.root)
            grand = self._getMax(self.root)
            diferencia = grand - peq
            self.delete(peq)
            self.delete(grand)
            if not self.search(diferencia):
                self.insert(diferencia)
        return self.root.key


for _ in range(int(input())):
    x = list(map(int, input().split()))
    tree = AVLTree()
    for i in x:
        if i != -1: tree.insert(i)        
    print(tree.particles())

