# Create studentnode structure as Class with data and pointer attributes.
class studentnode(object):
    def __init__(self, i, a = None):
        self.info = i # Node info variable
        self.contnode = a # Continue to next node variable
    
    def getnextnode (self): # get next node
        return self.contnode
    
    def new_next (self, a): # set the next node
        self.contnode = a
    
    def get_info (self): # Get node info
        return self.info
    
    def set_info (self, i): # Set Node info
        self.info = i

#Create Linked List Constructor Class 
class LinkedList(object):
    def __init__(self, b = None):
        self.root = b
        self.size = 0
    
    def takesize (self): # Get list size
        return self.size
    
    def addnewnode (self, i): # Function to add Node to root
        nnode = studentnode (i, self.root)
        self.root = nnode
        self.size += 1
    def delete (self, i): # Delete node and set previous node to deleted node's next node.
        currentnode =self.root
        lastnode = None
        while currentnode:
            if currentnode.get_info() == i:
                if lastnode:
                    lastnode.new_next(currentnode.getnextnode())
                else:
                    self.root = currentnode
                self.size -= 1
                return True, print(i, 'has been deleted from the linked list.') # Delete info
            else:
                lastnode = currentnode
                currentnode = currentnode.getnextnode()
        return False, print("Item cannot be located in linked list.") # Cannot locate info
    
    def locate (self, i): # locate new next node and get it.
        currentnode = self.root
        while currentnode:
            if currentnode.get_info() == i:
                return i, " has been located in the linked list."
            else:
                currentnode = currentnode.getnextnode()
        return "Node could not be located in linkedlist"
    
    #Create destructor method to delete all nodes in LinkedList
    def deleteall (self):
        clear = self.root
        if clear is None:
            print("\n Not possible to delete empty list")
        while clear:
            self.head = clear.getnextnode()
            clear = None
            clear = self.root
    
    #Create method to print all nodes in linked list.
    def printNode(self):
        node1 = self.root
        print("The node data in the linked list includes,")
        while node1:
            print(node1.info)
            node1 = node1.getnextnode()

# List Actions
newlist = LinkedList() # Create linked list object named new list
newlist.addnewnode(8) # Add new node
newlist.addnewnode(2) # Add new node
newlist.addnewnode(89) # Add new node
newlist.addnewnode(77) # Add new node
newlist.addnewnode(45) # Add new node
print("There are", newlist.size, "nodes in the linked list.")  # Print Linked List size before deletion.
newlist.printNode()
newlist.delete(8) # Delete '8' Node
print(newlist.locate(2)) # Locate "2" node in linked List
print(newlist.locate(89)) # Locate "89" node
print(newlist.locate(77)) # Locate "77" node
print(newlist.locate(555)) # Locate "77" node
print("There are", newlist.size, "nodes in the linked list.")  # Print Linked List size
newlist.printNode()
newlist.deleteall()
newlist.printNode()
newlist.deleteall()