class Node:

    def __init__(self):
        self.leftChild = None
        self.leftFlag = False
        self.data = None
        self.rightFlag = False
        self.rightChild = None


class threadedBinarytree:

    def __init__(self):
        self.root = None

    def isLeftmost(self, basePtr, ptr):
        if self.root is None:
            print("Error: Empty Tree")
            return 0
        elif not ptr.leftFlag:
            return 1
        elif basePtr == ptr:
            return 0
        else:
            basePtr = basePtr.left
            self.isLeftmost(basePtr, ptr)

    def isRightmost(self, basePtr, ptr):
        if self.root is None:
            print("Error: Empty Tree")
            return 0
        elif not ptr.rightFlag:
            return 1
        elif basePtr == ptr:
            return 0
        else:
            basePtr == ptr
            self.isRightmost()

    def inOrder(self, Tree):
        if self.root is None:
            print("Error: Empty Tree")
            return
        if Tree is None :
            self.inOrder(Tree.leftChild)
            print("ptr.data-> ", Tree.data)
            self.inOrder(Tree.rightChild)
        else:
            return

    def predecessor(self, Tree, ptr):
        if Tree is not None:
            self.inOrder(Tree.leftChild)
            print("ptr.data-> ", Tree.data)
            self.inOrder(Tree.rightChild)
            return None
        elif Tree.leftChild == ptr or Tree.rightChild == ptr:
            pass
        else:
            print("Error: Tree is empty.")

    def insertElement(self, ptr, value):
        global parent
        if self.root is None:
            newNode = Node()
            self.root = newNode
            newNode.data = value
            newNode.leftChild = dummy
            newNode.rightChild = dummy
            print(f"Root Node Address-> {self.root}\nNewNode Address-> {newNode}")
        elif ptr.data > value:
            if ptr.leftChild is None and ptr.rightChild is None:
                newNode = Node()
                ptr.leftFlag = not ptr.leftFlag
                ptr.leftChild = newNode
                newNode.data = value
                if self.isLeftmost(self.root, newNode):
                    newNode.leftChild = dummy
                else:
                    newNode.leftChild = self.predecessor()
                newNode.rightChild = self.successor()
            elif ptr.leftChild is None and ptr.rightChild is not None:
                newNode = Node()
                ptr.leftChild = newNode
                ptr.leftFlag = not ptr.leftFlag
                newNode.data = value
            else:
                parent = ptr
                ptr = ptr.leftChild
                self.insertElement(ptr, value)
        elif ptr.data < value:
            if ptr.rightChild is None and ptr.leftChild is None:
                newNode = Node()
                newNode.data = value
                ptr.rightChild = newNode
                ptr.rightChild = not ptr.rightFlag
            elif ptr.rightChild is None and ptr.leftChild is not None:
                newNode = Node()
                #           ptr.leftChild =
                newNode.data = value
                ptr.rightChild = newNode
                ptr.rightChild = not ptr.rightFlag
            else:
                parent = ptr
                ptr = ptr.rightChild
                self.insertElement(ptr, value)
        elif ptr.data == value:
            print("Error: Value is already present in the tree, Insertion is not possible.")

    def searchElement(self, ptr, value):
        if self.root is None:
            print("Error: Node not found. Empty Tree")
        elif ptr.data > value:
            ptr = ptr.leftChild
            self.searchElement(ptr, value)
        elif ptr.data < value:
            ptr = ptr.rightChild
            self.searchElement(ptr, value)
        elif ptr.data == value:
            print(f"Address of Node-> {ptr}\t\t\tValue at Node-> {ptr.data}")
            return ptr
        elif ptr is None:
            print("Error: value not found in tree")
            return -1


dummy = Node()
parent = None
tree = threadedBinarytree()
while True:
    choice = int(input(print("Enter your choice:-\n\t1.Insert node\n\t2.Search node\n\t3.Traverse Tree\n\tQuit")))
    if choice == 1:
        val = int(input(print("Enter value of node: ")))
        tree.insertElement(tree.root, val)
        parent = None
    elif choice == 2:
        val = int(input(print("Enter value to be searched")))
        tree.searchElement(tree.val)
