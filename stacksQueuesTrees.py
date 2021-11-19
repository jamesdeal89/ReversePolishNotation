# class for linked lists, stacks and queues
class Linkedlist():
    # the fucntions of a linked list mostly are pre-built into python itself.
    def __init__(self, userList):
        self.list = userList

    def pop(self, location):
        self.list.pop(location)

    def remove(self, value):
        self.list.remove(value)
    
    def append(self, value):
        self.list.append(value)
    
    def insert(self, value, location):
        self.list.insert(location, value)

class Queue():
    # First-in First-out
    def __init__(self) -> None:
        self.l = []
    
    def enqueue(self,value):
        self.l.insert(0,value)
    
    def dequeue(self):
        return self.l.pop(-1)

class Stack():
    # Last-in First-out basis
    def __init__(self) -> None:
        self.l = []

    def push(self, value):
        self.l.append(value)
    
    def POP(self):
        return self.l.pop(-1)
        # alternative version not using python in-built pop:
        # this creates a new list copy without the end value of the previous version,
        # essentially removing the last indexed item.
        # last = self.s[-1]
        # self.s = self.s[0:-1]
        # return last

    def top(self):
        return self.l[-1]

class Tree():
    def __init__(self) -> None:
        pass
    # add another node to tree
    # read value at end of pathway (huffman coding)
    # search tree for a value (depth/width methods)

class Node():
    """a node with a data value and 2 children or no children; for a binary tree"""
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

    def printData(self):
        print(self.data)

    def split(self, dataLeft, dataRight):
        """two children. each as variables which are themselves nodes with data can be inserted.
        This utilizes a recurrsive definition by referencing it's own class within the class."""
        self.left = Node(dataLeft)
        self.right = Node(dataRight)

    def printTreeDepth(self):
        """prints the entire tree from left to right down the tree including the current node via depth method."""
        # prints the current node.
        print(self.data)
        if self.left != None:
            """ as we made self.left a node itself we can use recurrsion again and the printTree() function again to print that data.
            When that finishes executing it'll go back to the previous 'self' reference in the above node and go to the right value.
            This printing uses depth method and goes all the way down the left before returning back up a layer and going down the right.
            Therefore printing all values in the tree."""
            # this prints the data on the left child and it's children in turn from left to right.
            self.left.printTreeDepth()
        if self.right != None:
            # this prints the data on the right child and it's children in turn from left to right.
            self.right.printTreeDepth()

    def printTreeBreadth(self):
        "this is the same as the other tree printing method however doing it layer by layer instead of via depth."
        print(self.data)
        if self.left != None:
            self.left.printData()
        if self.right != None: 
            self.right.printTreeBreadth()
            if self.left != None:
                self.left.printTreeBreadth()



"""
root = Node(20)
root.split(14,6)
root.left.split(10,4)
root.printTreeBreadth()


myStack = Stack()
myStack.push(5)
myStack.push(7)
myStack.push(9)
print(myStack)
print(myStack.POP())
print(myStack.top()) 

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue.dequeue())
print(myQueue.dequeue())
"""