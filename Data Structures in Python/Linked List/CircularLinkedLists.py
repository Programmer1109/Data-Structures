class Node:

    def __init__(self):
        self.data = int(input(print("Enter node value: ")))
        self.next = None

    def display(self):
        print("Node Value = ", self.data)


class circularLinkedList:

    def __init__(self):
        self.start = None

    def refresh(self):
        print("\tExecuting Refreshing Linked List")
        self.start = None
        print("Circular Linked List has been Refreshed")
    
    def getLength(self):
        print("Executing Length of Linked List")
        if self.start is not None:
            lenList = 1
            ptr = self.start
            while ptr.next != self.start:
                lenList = lenList + 1
                ptr = ptr.next
            return lenList
        else:
            print("Linked List is Empty")
            return 0

    def traversing(self):
        print("\tDisplaying Linked List")
        ptr = self.start
        if ptr is None:
            print("Linked List is Empty")
        else:
            while ptr.next != self.start:
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")

    def searching(self, value):
        print("\tExecuting Searching")
        ptr = self.start
        count = 1
        while ptr.next != self.start:
            if ptr.data == value:
                print("Search Successful")
                return count
            else:
                ptr = ptr.next
                count = count + 1
        print(f"Node Value = {ptr.data}")
        if ptr.data == value:
            print("Search Successful")
            return count
        else:
            print("Unsuccessful")
            return -1

    def insertBegin(self):
        print("\tExecuting Insert Begin")
        newNode = Node()
        if self.start != None:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            newNode.next = self.start
            print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            self.start = newNode
            ptr.next = self.start
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        else:
            newNode.next = newNode
            print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            self.start = newNode
            # print(f"Ptr -> {self.start}\t{self.data}\t{self.next}")

    def insertBeforenode(self, targetNode):
        print("\tExecuting Insert Before Node")
        newNode = Node()
        flag = self.searching(targetNode.data)
        print(flag)
        if flag != -1:
            if targetNode != self.start:
                ptr = self.start
                prevPtr = None
                while ptr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                print(f"Previous Ptr -> {prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
                prevPtr.next = newNode
                print(f"Previous Ptr -> {prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
                newNode.next = targetNode
                print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            else:
                ptr = self.start
                while ptr.next != self.start:
                    ptr = ptr.next
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                newNode.next = self.start
                print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
                self.start = newNode
                ptr.next = self.start
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        else:
            print("Error: Input node not present in the list.")

    def insertAfternode(self, targetNode):
        print("\tExecuting Insert After Node")
        newNode = Node()
        flag = self.searching(targetNode.data)
        print(flag)
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
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                ptr.next = newNode
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                newNode.next = nextPtr
                print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            elif targetNode == ptr:
                ptr = self.start
                while ptr.next != self.start:
                    ptr = ptr.next
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                newNode.next = ptr.next
                print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
                ptr.next = newNode
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        else:
            print("Error: Input node is not present in the Linked List.")

    def insertEnd(self):
        print("\tExecuting Insert at End")
        newNode = Node()
        if self.start is not None:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            newNode.next = self.start
            print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            ptr.next = newNode
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        else:
            newNode.next = newNode
            print(f"New Node -> {newNode}\t{newNode.data}\t{newNode.next}")
            self.start = newNode

    def delete_startNode(self):
        print("\tExecuting Delete Start Node")
        if self.start is not None:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            ptr.next = self.start.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            self.start = ptr.next
            print(f"Start Node -> {self.start}\t{self.start.data}\t{self.start.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")

    def delete_node_before(self, targetNode):
        print("\tExecuting Delete Node Before")
        flag = self.searching(targetNode.data)
        if flag > 2:
            ptr = self.start
            nextPtr = ptr.next
            while nextPtr.next != targetNode:
                ptr = ptr.next
                nextPtr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            ptr.next = nextPtr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        elif flag == 1:
            print("Error: There is no node before this node. Hence, deletion can't be performed.")
        elif flag == 2:
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            ptr.next = self.start.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            self.start = ptr.next
            print(f"Start Node -> {self.start}\t{self.start.data}\t{self.start.next}")
        elif flag == -1:
            print("Error: Node to be deleted is not present in the list.")

    def delete_node_after(self, targetNode):
        print("Executing Delete After Node")
        flag = self.searching(targetNode.data)
        print("f= ", flag)
        length = self.getLength()
        print("l= ", length)
        if flag != -1:
            if flag < length - 1:
                ptr = self.start
                prevPtr = None
                while prevPtr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                prevPtr.next = ptr.next
            elif flag == length - 1:
                ptr = self.start
                prevPtr = self.start
                while ptr.next != self.start:
                    prevPtr = ptr
                    ptr = ptr.next
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
                prevPtr.next = self.start
                print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")    
            elif flag == length:
                print("Error: There is no node present after this. Hence, deletion operation can't be performed.")
        else:
            print("Error: Node to be deleted is not present in the list.")

    def delete_endNode(self):
        print("Executing Delete End Node")
        if self.start is not None:
            ptr = self.start
            prevPtr = self.start
            while ptr.next != self.start:
                prevPtr = ptr
                ptr = ptr.next
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
            prevPtr.next = self.start
            print(f"Ptr -> {ptr}\t{ptr.data}\t{ptr.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")


students = circularLinkedList()
while True:
    print("Choose your operation:- \n\t1. Insert node at start\n\t2. Insert node at the end\n\t3. Insert node before a node\n\t4. Insert node after a node")
    print("\t5. Delete node at start\n\t6. Delete node at end\n\t7. Delete node before a node\n\t8. Delete node after node\n\t9. Length of Linked List")
    print("\t10. Search node\n\t11. Display Linked List\n\t12. Refresh\n\t13. Quit")
    choice = int(input(print("Enter your choice:- ")))

    if choice == 1:
        students.insertBegin()
    elif choice == 2:
        students.insertEnd()
    elif choice == 3:
        value = int(input(print("Enter the value at node before which element is to be inserted: ")))
        sign = students.searching(value)
        if sign != -1:
            ptr = students.start
            for iter in range(1, sign):
                ptr = ptr.next
            students.insertBeforenode(ptr)
        else: 
            print("Error! the entered value is not present in the linked list.")
    elif choice == 4:
        value = int(input(print("Enter the value at node after which element is to be inserted: ")))
        sign = students.searching(value)
        if sign != -1:
            ptr = students.start
            for iter in range(sign-1):
                ptr = ptr.next
            students.insertAfternode(ptr)
        else:
            print("Error! the entered value is not present in the linked list.")
    elif choice == 5:
        students.delete_startNode()
    elif choice == 6:
        students.delete_endNode()
    elif choice == 7:
        value = int(input(print("Enter the value at node before which element is to be deleted: ")))
        sign = students.searching(value)
        if sign != -1:
            ptr = students.start
            for iter in range(sign-1):
                ptr = ptr.next
            students.delete_node_before(ptr)
        else:
            print("Error! the entered value is not present in linked list.")
    elif choice == 8:
        value = int(input(print("Enter the value at node after which element is to be deleted: ")))
        sign = students.searching(value)
        if sign != -1:
            ptr = students.start
            for iter in range(sign-1):
                ptr = ptr.next
            students.delete_node_after(ptr)
        else:
            print("Entered element is not present in the linked list.")
    elif choice == 9:
        length_list = students.getLength()
        print(f"length of Linked List = {length_list}")
    elif choice == 10:
        value = int(input(print("Enter value to be searched: ")))
        sign = students.searching(value)
        if sign != -1:
            print(f"Entered value was found at node {sign}")
        else:
            print("Error! entered value is not present in the list")
    elif choice == 11:
        students.traversing()
    elif choice == 12:
        students.refresh()
    elif choice == 13:
        exit()
    else:
        print("Error!!! You've entered an invalid input.")
