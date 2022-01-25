class Node:
    def __init__(self):
        self.prev = None
        self.data = input(print("Enter data: "))
        self.next = None


class Deque:
    def __init__(self):
        self.start = None
        self.end = None

    def refresh(self):
        while self.start is not None:
            self.start = self.start.next

    def peek(self):
        if self.start is None:
            print(None)
        else:
            print(self.start.data)

    def display(self):
        print(self.start)
        if self.start is not None:
            print("inside if else...")
            ptr = self.start
            while ptr.next is not None:
                print(f"{ptr.prev}\t\t{ptr}\t\t{ptr.next}\t\t{ptr.data}")
                # print(ptr.data)
                ptr = ptr.next
            print(f"{ptr.prev}\t\t{ptr}\t\t{ptr.next}\t\t{ptr.data}")
            # print(ptr.data)
        else:
            print("Error: no elements to show")

    def insertStart(self):
        print("in insertStart...")
        newNode = Node()
        print("startNode: before -> ", self.start)
        print("newNode = ", newNode)
        if self.start is None:
            print("Inserting in Empty Queue")
            self.start = newNode
            print("startNode: after -> ", self.start)
        else:
            newNode.next = self.start
            self.start.prev = newNode
            self.start = newNode

            print("startNode: after -> ", self.start)

    def insertEnd(self):
        print("in insertEnd...")
        newNode = Node()
        print(newNode)
        print("data at new node is ", newNode.data)
        print("startNode: before -> ", self.start)
        if self.start is None:
            self.start = newNode
            print("startNode: after -> ", self.start)
        else:
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode
            newNode.prev = ptr

    def deleteStart(self):
        print("in deleteStart...")
        if self.start is None:
            print("Error: can't delete element from an empty deque.")
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

    def deleteEnd(self):
        print("in deleteEnd...")
        if self.start is None:
            print("Error: can't delete element from an empty deque")
        elif self.start.next is None:
            self.start = None
        else:
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            ptr = ptr.prev
            ptr.next = None


def inputRestricted():
    print("in inputRestricted...")
    queue = Deque()
    option = int(input(print("Enter your choice:\n\t1.Insert\n\t2.Delete from left\n\t3.Delete from right\n\t4.Display"
                             "\n\t5.Refresh ")))
    while True:
        if option == 1:
            queue.insertEnd()
        elif option == 2:
            queue.deleteStart()
        elif option == 3:
            queue.deleteEnd()
        elif option == 4:
            queue.display()
        elif option == 5:
            queue.peek()
        elif option == 6:
            queue.refresh()
        elif option == 7:
            exit()
        else:
            print("invalid choice")
        option = int(input(print("Enter your choice:\n\t1.Insert\n\t2.Delete from left\n\t3.Delete from right\n\t"
                                 "4.Display\n\t5.Peek\n\t6.Refresh\n\t7.Quit")))


def outputRestricted():
    print("in outputRestricted...")
    queue = Deque()
    option = int(input(print("Enter your choice:\n\t1.Insert at Start\n\t2.Insert at End\n\t3.Delete\n\t4.Display"
                             "\n\t5.Peek\n\t6.Refresh\n\t7.Quit")))
    while True:
        if option == 1:
            queue.insertStart()
        elif option == 2:
            queue.insertEnd()
        elif option == 3:
            queue.deleteStart()
        elif option == 4:
            queue.display()
        elif option == 5:
            queue.peek()
        elif option == 6:
            queue.refresh()
        elif option == 7:
            exit()
        else:
            print("invalid choice")
        option = int(input(print("Enter your choice:\n\t1.Insert at Start\n\t2.Insert at End\n\t3.Delete\n\t4.Display"
                                 "\n\t5.Peek\n\t6.Refresh\n\t7.Quit")))


choice = int(input(print("Enter your choice:\n\t1.Input Restricted Queue\n\t2.Output Restricted Queue")))
if choice == 1:
    inputRestricted()
elif choice == 2:
    outputRestricted()
else:
    print("Invalid Choice")
