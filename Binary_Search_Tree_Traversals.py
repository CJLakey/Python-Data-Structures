class Tree: # Create Tree Class
    def __init__(self, data): #Create Constructor
        self.data = data # Node value attribute
        self.left = None # Node right pointer attribute
        self.right = None # Node Left pointer atribute
    
    def add_left(self, data): # create add_left node method
        if self.left == None: # if left attribute of node is null
            self.left = Tree(data) # Create new left node and set pointer to node value
        else: 
            newnode = Tree(data) # newnode variable equals new node data value.
            newnode.left = self.left # newnode left value equals left attribute pointer
            self.left = newnode # left attribute pointer equals newnode variable
    
    def add_right(self, data): # create add_left node method
        if self.right == None: # if right attribute of node is null
            self.right = Tree(data) # Create new right node and set pointer to node value
        else:
            newnode = Tree(data) # newnode variable equals new node data value.
            newnode.right = self.right # newnode left value equals left attribute pointer
            self.right = newnode # left attribute pointer equals newnode variable
# Traversals
    def preorder(self):
        print(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()
        
        print(self.data)


# Tree Structure
#         |100|
#       /       \
#    |60|      |110|
#   /    \    /    \
# |50|  |67||109|  |111| 
#
# Code Creating above structure.

root = Tree('100') # Set Root Node to 100
root.add_left('60')    # Set root node left child to 60
root.add_right('110')   # Set root node right child to 110

firstLeft = root.left # Set root node left child "60" to firstLeft variable
firstLeft.add_left('50') # Set firstLeft left child to 50
firstLeft.add_right('67') # Set firstLeft right child to 67

firstRight = root.right # Set root node right child "110" to firstRight variable
firstRight.add_left('109') # Set firstRight left child to 109
firstRight.add_right('111')  # Set firstRight right child to 111
print("Preorder Traversal:")
print(root.preorder())
print("\n")
print("Inorder Traversal:")
print(root.inorder())
print("\n")
print("Postorder Traversal:")
print(root.postorder())