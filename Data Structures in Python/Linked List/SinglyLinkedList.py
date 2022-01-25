class Node:

    def __init__(self):
        self.data = input(print("Enter data: "))
        self.next = None

    def display(self):
        print("Student id = ", self.data)


class linkedList:

    def __init__(self):
        self.start = None

    def getLength(self):
        if self.start is not None:
            count = 1
            ptr = self.start
            while ptr.next is not None:
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
            while ptr is not None:
                print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                # print(ptr.data)
                ptr = ptr.next

    def searching(self, value):
        ptr = self.start
        count = 1
        while ptr is not None:
            if ptr.data == value:
                return count
            else:
                ptr = ptr.next
                count = count + 1
        return -1

    def refresh(self):
        self.start = None
        print("The Linked List has been refreshed by user.")
        
    def insertBegin(self):
        newNode = Node()
        # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
        newNode.next = self.start
        self.start = newNode                        
        # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
        # print(f"{newNode}\t{newNode.data}\t{newNode.next}")

    def insertBeforenode(self, targetNode):
        newNode = Node()
        flag = self.searching(targetNode.data)
        if flag != -1:
            if targetNode != self.start:
                ptr = self.start
                prevPtr = None
                while ptr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
                prevPtr.next = newNode
                # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
                newNode.next = ptr
                # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
            else:
                # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
                newNode.next = self.start
                # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
                self.start = newNode
                # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")

    def insertAfternode(self, targetNode):
        newNode = Node()
        flag = self.searching(targetNode.data)
        if flag != -1:
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            if targetNode != ptr:
                ptr = self.start
                nextPtr = ptr.next
                while ptr != targetNode:
                    ptr = ptr.next
                    nextPtr = ptr.next
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                ptr.next = newNode
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                newNode.next = nextPtr
                # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
            else:
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                ptr.next = newNode
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                newNode.next = None    
                # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")

    def insertEnd(self):
        if self.start is not None:
            newNode = Node()                           
            newNode.next = None
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            ptr.next = newNode
            # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
        else:
            newNode = Node()
            # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
            newNode.next = self.start
            self.start = newNode                        
            # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
            # print(f"{newNode}\t{newNode.data}\t{newNode.next}")

    def delete_startNode(self):
        if self.start is not None:
            # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
            ptr = self.start
            self.start = ptr.next
            # print(f"{self.start}\t{self.start.data}\t{self.start.next}")
            # print(f"{newNode}\t{newNode.data}\t{newNode.next}")
        else:
            print("Error: Linked List is empty and hence, no deletion can be performed.")

    def delete_node_before(self, targetNode):
        print(f"{targetNode}\t{targetNode.data}\t{targetNode.next}")
        flag = self.searching(targetNode.data)
        if flag > 2:
            ptr = self.start
            nextPtr = ptr.next
            while nextPtr.next != targetNode:
                ptr = ptr.next
                nextPtr = ptr.next
            print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            print(f"{nextPtr}\t{nextPtr.data}\t{nextPtr.next}")
            ptr.next = nextPtr.next
            print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            print(f"{nextPtr}\t{nextPtr.data}\t{nextPtr.next}")
        elif flag == 1:
            print("Error: There is no node before this node. Hence, deletion can't be performed.")
        elif flag == 2:
            self.delete_startNode()
        elif flag == -1:
            print("Error: Node to be deleted is not present in the list.")

    def delete_node_after(self, targetNode):
        print(f"{targetNode}\t{targetNode.data}\t{targetNode.next}")
        flag = self.searching(targetNode.data)
        length = self.getLength()
        if flag != -1:
            if flag < length - 1:
                ptr = self.start
                prevPtr = None
                while prevPtr != targetNode:
                    prevPtr = ptr
                    ptr = ptr.next
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
                prevPtr.next = ptr.next
                # print(f"{ptr}\t{ptr.data}\t{ptr.next}")
                # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
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
            while ptr.next is not None:
                prevPtr = ptr
                ptr = ptr.next
            # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
            prevPtr.next = None
            # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")


node_object = linkedList()
while True:
    choice = int(input(print("Enter your choice:-\n\t1.Insert at start\n\t2.Insert at end\n\t3.Insert before node\n\t4.Insert after node\n\t5.Delete at start\n\t6.Delete at end\n\t7.Delete before node\n\t8.Delete after node\n\t9.Length of linked list\n\t10.Search element\n\t11.Display\n\t12.Refresh\n\t13.Quit"))) 
    if choice == 1:
        node_object.insertBegin()
    elif choice == 2:
        node_object.insertEnd()
    elif choice == 3:
        valNode = input(print("Enter the value at node before which element has to be inserted: "))
        sign = node_object.searching(valNode)
        if sign == -1:
            print("Error: No element with the assigned value exists in the list.")
        else:
            pointer = node_object.start
            for iter in range(sign-1):
                pointer = pointer.next
            node_object.insertBeforenode(pointer)
    elif choice == 4:
        valNode = input(print("Enter the value at node after which element has to be inserted: "))
        sign = node_object.searching(valNode)
        if sign == -1:
            print("Error: No element with the assigned value exists in the list.")
        else:
            pointer = node_object.start
            for iter in range(1, sign):
                pointer = pointer.next
            node_object.insertAfternode(pointer)
    elif choice == 5:
        node_object.delete_startNode()
    elif choice == 6:
        node_object.delete_endNode()
    elif choice == 7:
        valNode = input(print("Enter value at node the element before which is to be deleted : "))
        sign = node_object.searching(valNode)
        if sign == -1:
            print("Error: No element with the assigned value exists in the list.")
        else:
            pointer = node_object.start
            for iter in range(sign-1):
                pointer = pointer.next
            node_object.delete_node_before(pointer)
    elif choice == 8:
        valNode = input(print("Enter value at node the element after which is to be deleted : "))
        sign = node_object.searching(valNode)
        if sign == -1:
            print("Error: No element with the assigned value exists in the list.")
        else:
            pointer = node_object.start
            for iter in range(sign-1):
                pointer = pointer.next
            node_object.delete_node_after(pointer)
    elif choice == 9:
        length_LinkedList = node_object.getLength()
        print(f"Length of Linked List = {length_LinkedList}")
    elif choice == 10:
        valNode = input(print("Enter the value at node which is to be searched: "))
        sign = node_object.searching(valNode)
        if sign == -1:
            print("Error: the entered element is not found in the Linked List")
        else: 
            print(f"Entered element found at {sign}")
    elif choice == 11:
        node_object.traversing()
    elif choice == 12:
        node_object.refresh()
    elif choice == 13:
        exit()
    else:
        print("Invalid choice")

