class Node:

    def __init__(self):
        self.leftChild = None
        self.data = None
        self.rightChild = None


class binarySearchtree:

    def __init__(self):
        self.root = None
        
    def miniElement(self, ptr):
        while ptr.leftChild is not None:
            ptr = ptr.leftChild
        return ptr

    def maxElement(self, ptr):
        while ptr.rightChild is not None:
            ptr = ptr.rightChild
        return ptr

    def preOrder(self, Tree):
        if Tree is not None:
            print("ptr.data-> ", Tree.data)
            self.preOrder(Tree.leftChild)
            self.preOrder(Tree.rightChild)

    def inOrder(self, Tree):
        if self.root is not None:
            self.inOrder(Tree.leftChild)
            print("ptr.data-> ", Tree.data)
            self.inOrder(Tree.rightChild)

    def postOrder(self, Tree):
        if self.root is not None:
            self.inOrder(Tree.leftChild)
            self.inOrder(Tree.rightChild)
            print("ptr.data-> ", Tree.data)

    def heightTree(self, Tree):
        global height
        if Tree is None:
            return 0
        leftHeight = self.heightTree(Tree.leftChild)
        rightHeight = self.heightTree(Tree.rightChild)
        if leftHeight > rightHeight:
            height = leftHeight + 1
        else:
            height = rightHeight + 1
        return height

    def totalNodes(self, Tree):
        if Tree is None:
            return 1
        else:
            return self.totalNodes(Tree.leftChild) + self.totalNodes(Tree.rightChild) + 1

    def internalNodes(self, Tree):
        if Tree.leftChild is None and Tree.rightChild is None:
            return 0
        else:
            return self.internalNodes(Tree.leftChild) + self.internalNodes(Tree.rightChild) + 1

    def leafNodes(self, Tree):
        if Tree is None:
            return 0
        elif Tree.rightChild is None and Tree.leftChild is None:
            return 1
        else:
            return self.leafNodes(Tree.leftChild) + self.leafNodes(Tree.rightChild)

    def mirrorImage(self, ptr):
        if self.root is None:
            print("Error: Empty Tree. No nodes to display.")
        elif ptr is not None:
            if not ptr.leftChild and not ptr.rightChild:
                return
            else:
                self.mirrorImage(ptr.leftChild)
                self.mirrorImage(ptr.rightChild)
                temp = ptr.leftChild
                ptr.leftChild = ptr.rightChild
                ptr.rightChild = temp
        else:
            return

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

    def insertElement(self, ptr, value):
        if self.root is None:
            newNode = Node()
            self.root = newNode
            newNode.data = value
            print(f"Root Node Address-> {self.root}\nNewNode Address-> {newNode}")
        elif ptr.data > value:
            if ptr.leftChild is None:
                newNode = Node()
                ptr.leftChild = newNode
                newNode.data = value
            else:
                ptr = ptr.leftChild
                self.insertElement(ptr, value)
        elif ptr.data < value:
            if ptr.rightChild is None:
                newNode = Node()
                ptr.rightChild = newNode
                newNode.data = value
            else:
                ptr = ptr.rightChild
                self.insertElement(ptr, value)
        elif ptr.data == value:
            print("Error: Value is already present in the tree, Insertion is not possible.")

    def deleteElement(self, ptr, value):
        global prevPtr
        if self.root is None:
            print("Error: No element to delete. Empty Tree")
            return
        ptr = self.searchElement(ptr, value)
        if ptr != -1:
            if ptr.leftChild is None and ptr.rightChild is None:
                if prevPtr.leftChild == ptr:
                    prevPtr.leftChild = None
                elif prevPtr.rightChild == ptr:
                    prevPtr.rightChild = None
            elif ptr.leftChild is not None and ptr.rightChild is None:
                if prevPtr.leftChild == ptr:
                    prevPtr.leftChild = ptr.leftChild
                elif prevPtr.rightChild == ptr:
                    prevPtr.rightChild = ptr.leftChild
            elif ptr.leftChild is None and ptr.rightChild is not None:
                if prevPtr.leftChild == ptr:
                    prevPtr.leftChild = ptr.rightChild
                elif prevPtr.rightChild == ptr:
                    prevPtr.rightChild = ptr.rightChild
            elif ptr.leftChild is not None and ptr.rightChild is not None:
                pointer = self.miniElement(ptr.rightChild)
                if pointer.rightChild is None:
                    ptr.data = pointer.data
                    self.deleteElement(self.root, pointer.data)
                else:
                    ptr.data = pointer.data
                    self.deleteElement(self.root, pointer.data)

        else:
            print("Error: Entered element is not present in the tree.")


tree = binarySearchtree()
prevPtr = None
height = 0
while True:
    choice = int(input(print("Enter your choice:-\n\t1.Insert element in BST\n\t2.Pre Order Traversal\n\t3.In Order "
                             "Traversal\n\t4.Post Order Traversal\n\t5.Search element in BST\n\t6.Delete element in BST"
                             "\n\t7.Total no. of nodes\n\t8.No. of Internal nodes\n\t8.No. of Leaf nodes\n\t9.Height of"
                             " Tree\n\t10.Mirror Image of Tree\n\t11.Smallest Element in Tree\n\t12.Largest Element in "
                             "Tree\n\t13.Delete entire Tree\n\t14.Quit\n\t")))
    if choice == 1:
        val = int(input(print("Enter value to be inserted in tree: ")))
        tree.insertElement(tree.root, val)
    elif choice == 2:
        tree.preOrder(tree.root)
    elif choice == 3:
        tree.inOrder(tree.root)
    elif choice == 4:
        tree.postOrder(tree.root)
    elif choice == 5:
        tree.searchElement(tree.root, val)
    elif choice == 6:
        tree.deleteElement(tree.root, val)
        prevPtr = None
    elif choice == 10:
        exit()
    else:
        print("Invalid Choice!!!")
