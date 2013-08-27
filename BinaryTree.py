# Binary Search Tree
# WARNING: This code does not actually work. Use at your own risk!

class Node:

    # initializes what a node is by setting up left and right nodes
    # self.data refers to the top node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(Node):

    # the binary tree is based on the node system
    # we start off with a tree without nodes
    def __init__(self):
        self.root = None

    # to be used later in insert() so that we may insert new node
    def addNode(self, data):
        return Node(data)

    # we insert a new node to the tree with appropriate data
    def insert(self, item):
        # checks if there is a root node
        if self.root == None:
            self.root = Node(item)
        else:
            if item < self.root.data:
                if self.root.left == None:
                    self.root.left = Node(item)
                else:
                    self.root.left.insert(item)
            else: # data greater than the root data
                if self.root.right == None:
                    self.root.right = Node(item)
                else:
                    self.root.right.insert(item)

    # searches for item in the tree
    def search(self, item):
        if self.root == None: # if the tree is empty
            return "Not found"
        elif self.root == item: # if the data in the root is the item
            return "Found"
        # if the data is smaller than that in the root
        elif item < self.root.data: 
            search(self.root.left, item)            
        else: # the data is larger than that in the root
            search(self.root.right, item)


# main

