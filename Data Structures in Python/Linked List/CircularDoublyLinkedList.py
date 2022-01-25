class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class doublyLinkedlist:

    def __init__(self):
        self.start = None

    def getLength(self):
        if self.start is not None:
            count = 1
            ptr = self.start
            while ptr.next != self.start:
                count = count + 1
                ptr = ptr.next
            return count
        else:
            print("Linked List is Empty")
            return 0

    def traversing(self):
        ptr = self.start
        if ptr is None:
            print("Empty List ")
        else:
            while ptr.next != self.start:
                print(f"{ptr.prev}\t{ptr.data}\t{ptr.next}\t{ptr}")
                ptr = ptr.next
            print(f"{ptr.prev}\t{ptr.data}\t{ptr.next}\t{ptr}")

    def searching(self, value):
        ptr = self.start
        count = 1
        if ptr.data == value:
            return count
        else:
            ptr = ptr.next
            while ptr != self.start:
                if ptr.data == value:
                    return count
                else:
                    ptr = ptr.next
                    count = count + 1
            return -1

    def insertBegin(self, newNode):
        ptr = self.start
        while ptr.next != self.start:
            ptr = ptr.next
        ptr.next = newNode
        newNode.prev = ptr
        newNode.next = self.start
        self.start = newNode

    def insertBeforenode(self, targetNode, newNode):
        flag = self.searching(targetNode.data)
        if flag != -1:
            if targetNode != self.start:
                ptr = self.start
                prevPtr = None
                while ptr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                prevPtr.next = newNode
                newNode.prev = prevPtr
                ptr.prev = newNode
                newNode.next = ptr
            else:
                self.insertBegin(newNode)
        else:
            print("Error: Node to be deleted is not present in the list.")

    def insertAfternode(self, targetNode, newNode):
        flag = self.searching(targetNode.data)
        if flag != -1:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            if targetNode != ptr:
                ptr = self.start
                nextPtr = ptr.next
                while ptr != targetNode:
                    ptr = ptr.next
                    nextPtr = ptr.next
                nextPtr.prev = newNode
                newNode.next = nextPtr
                ptr.next = newNode
                newNode.prev = ptr
            elif targetNode == ptr:
                self.insertEnd(newNode)
        else:
            print("Error: Node to be deleted is not present in the list.")

    def insertEnd(self, newNode):
        newNode.next = self.start
        ptr = self.start
        while ptr.next != self.start:
            ptr = ptr.next
        ptr.next = newNode
        self.start.prev = newNode
        newNode.prev = ptr
        newNode.next = self.start

    def delete_startNode(self):
        if self.start is not None:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            ptr.next = self.start.next
            self.start = self.start.next
            self.start.prev = ptr
        else:
            print("Error: Node to be deleted is not present in the list.")

    def delete_node_before(self, targetNode):
        flag = self.searching(targetNode.data)
        if flag > 2:
            ptr = self.start
            nextPtr = ptr.next
            while nextPtr.next != targetNode:
                ptr = ptr.next
                nextPtr = ptr.next
            ptr.next = nextPtr.next
        elif flag == 1:
            print("Error: There is no node before this node. Hence, deletion can't be performed.")
        elif flag == 2:
            self.delete_startNode()
        elif flag == -1:
            print("Error: Node to be deleted is not present in the list.")

    def delete_node_after(self, targetNode):
        flag = self.searching(targetNode.data)
        length = self.getLength()
        if flag != -1:
            if flag < length - 1:
                ptr = self.start
                prevPtr = None
                while prevPtr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                prevPtr.next = ptr.next
            elif flag == length - 1:
                self.delete_endNode()
            elif flag == length:
                print("Error: There is no node present after this. Hence, deletion operation can't be performed.")
        else:
            print("Error: Node to be deleted is not present in the list.")

    def delete_endNode(self):
        if self.start is not None:
            ptr = self.start
            prevPtr = self.start
            while ptr.next != self.start:
                prevPtr = ptr
                ptr = ptr.next
            prevPtr.next = self.start
            self.start.prev = prevPtr
        else:
            print("Error: Node to be deleted is not present in the list.")


student1 = Node('A')
student2 = Node('B')
student3 = Node('C')
student1.next = student2
student1.prev = student3
student2.next = student3
student2.prev = student1
student3.next = student1
student3.prev = student2

sciClass = doublyLinkedlist()
sciClass.start = student1
print("\t\t\t\t\t ptr.prev \t\t\t\t ptr.data \t\t\t\t\t ptr.next \t\t\t\t\t\t ptr")
sciClass.traversing()
print("\tInserting at beginning!!! ")
student4 = Node('D')
student9 = Node('I')
sciClass.insertBegin(student4)
sciClass.traversing()
print("\tInserting at beginning!!! ")
sciClass.insertBegin(student9)
sciClass.traversing()
print("\tInserting at ending!!!")
student5 = Node('E')
sciClass.insertEnd(student5)
sciClass.traversing()
print("\tInserting before node!!! ")
student6 = Node('F')
sciClass.insertBeforenode(student1, student6)
sciClass.traversing()
print(" \tInserting after node!!!")
student7 = Node('G')
sciClass.insertAfternode(student3, student7)
sciClass.traversing()
print("\tInserting after node!!!")
student8 = Node('H')
sciClass.insertAfternode(student3, student8)
sciClass.traversing()

dummy = sciClass.searching('E')
print("\tDeleting starting node!!!")
sciClass.delete_startNode()
# sciClass.delete_node_before(student2)
sciClass.traversing()
print("\tDeleting after node!!!")
sciClass.delete_node_after(student2)
sciClass.traversing()
print("\tDeleting before node!!!")
sciClass.delete_node_before(student2)
sciClass.traversing()
print("\tDeleting ending node!!!")
sciClass.delete_endNode()
sciClass.traversing()
print("\t\tEnd ")
