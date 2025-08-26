from collections import deque

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        current = self.root
        while current.info != val:
            if val < current.info:
                if current.left is None:
                    current.left = Node(val)
                current = current.left
            else:  #  val > current.info:
                if current.right is None:
                    current.right = Node(val)
                current = current.right
        return None

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def levelOrder(root):
    q = deque([root])
    vals = []
    while q:
        curr = q.popleft()
        vals.append(str(curr.info))
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    print(' '.join(vals))
    return None


tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    tree.create(arr[i])
levelOrder(tree.root)