class Node:

    def __init__(self):
        self.previous = None
        self.next = None
        self.data = input(print("Enter data:- "))



class enqueueRestrictedQueue:

    def __init__(self):
        self.start = None

    def enqueueLast(self):
        print("Inside Enqueue at End...")
        newNode = Node()
        print("newNode = ", newNode)
        if self.start is None:
            print("Inserting in Empty Queue")
            self.start = newNode
            print(f"Last Node: after -> {self.start}   {self.start.data}")
        else:
            pointer = self.start
            while pointer.next is not None:
                pointer = pointer.next
            print(f"Last Node: before -> {pointer}   {pointer.data}")
            pointer.next = newNode
            newNode.previous = pointer
            print(f"Last Node: after -> {pointer.next} {newNode.data}")
    
    def dequeueFront(self):
        print("Inside Dequeue at the Front...")
        if self.start is None:
            print("Underflow Error:- Can't delete element from an empty Deque")
        elif self.start.next is None:
            print(f"Start Node: before -> {self.start}   {self.start.data}")
            self.start = None
            print(f"Start Node: after -> {self.start}")
        else:
            print(f"Start Node: before -> {self.start}   {self.start.data}")
            self.start = self.start.next
            self.start.previous = None
            print(f"Start Node: after -> {self.start}   {self.start.data}")

    def dequeueLast(self):
        print("Inside Dequeue at the End...")
        if self.start is None:
            print("Underflow Error:- Can't delete element from an empty Queue")
        elif self.start.next is None:
            print(f"Last Node: before -> {self.start}   {self.start.data}")
            self.start = None
            print(f"Last Node: after -> {self.start}")
        else:
            pointer = self.start 
            while pointer.next is not None:
                pointer = pointer.next
            print(f"Last Node: before -> {pointer}   {pointer.data}")
            pointer = pointer.previous
            print(f"Last Node: after -> {pointer}   {pointer.data}")
            pointer.next = None

    def display(self):
        print(self.start)
        if self.start is not None:
            print("Inside IF else...")
            pointer = self.start
            while pointer.next is not None:
                print(f"Pointer:- {pointer.previous}\t\t{pointer}\t\t{pointer.next}\t\t{pointer.data}")
                pointer = pointer.next
            print(f"Pointer:- {pointer.previous}\t\t{pointer}\t\t{pointer.next}\t\t{pointer.data}")
            print(pointer.data)
        else:
            print("Error: no elements to show")

    def peek(self):
        if self.start is None:
            print("Error:- Can't peek in an empty List!!!")
        else:
            print("Peek Value = ", self.start.data)

    def refresh(self):
        while self.start is not None:
            self.start = self.start.next



class dequeueRestrictedQueue:

    def __init__(self):
        self.start = None
    
    def enqueueFront(self):
        print("Inside Enqueue at Front...")
        newNode = Node()
        if self.start is None:
            print("Inserting in Empty Queue")
            print(f"Start Node:- before -> {self.start}")
            self.start = newNode
            print(f"Start Node: after -> {self.start}   {self.start.data}")
        else:
            print(f"Start Node:- before -> {self.start}   {self.start.data}")
            newNode.next = self.start
            self.start.previous = newNode
            self.start = newNode
            print(f"Start Node: after -> {self.start}   {self.start.data}")
    
    def enqueueLast(self):
        print("In Enqueue at Last...")
        newNode = Node()
        if self.start is None:
            print(f"Last Node: before -> {self.start}")
            self.start = newNode
            print(f"Last Node: after -> {self.start}   {self.start.data}")
        else:
            pointer = self.start
            while pointer.next is not None:
                pointer = pointer.next
            print(f"Last Node: before -> {pointer}   {pointer.data}")
            pointer.next = newNode
            print(f"Last Node: after -> {pointer.next}   {newNode.data}")
            newNode.previous = pointer

    def dequeueFront(self):
        if self.start is None:
            print("Underflow Error:- Can't delete element from an Empty Deque.")
        elif self.start.next is None:
            print(f"Start Node: before -> {self.start}   {self.start.data}")
            self.start = None
            print(f"Start Node: after -> {self.start}")
        else:
            print(f"Start Node: before -> {self.start}   {self.start.data}")
            self.start = self.start.next
            self.start.previous = None
            print(f"Start Node: after -> {self.start}   {self.start.data}")
    
    def display(self):
        print(self.start)
        if self.start is not None:
            print("inside if else...")
            pointer = self.start
            while pointer.next is not None:
                print(f"Pointer:- {pointer.previous}   {pointer}   {pointer.next}   {pointer.data}")
                pointer = pointer.next
            print(f"Pointer:- {pointer.previous}   {pointer}   {pointer.next}   {pointer.data}")
            # print(pointer.data)
        else:
            print("Error: no elements to show")

    def peek(self):
        if self.start is None:
            print("Error:- Can't peek into an Empty List")
        else:
            print("Peek Value = ", self.start.data)

    def refresh(self):
        while self.start is not None:
            self.start = self.start.next



#                                MAIN PROGRAM STARTS HERE
choice = int(input(print("Enter your choice:\n\t1.Input Restricted Queue\n\t2.Output Restricted Queue")))
if choice == 1:
    print("********************\tINPUT RESTRICTED DEQUE QUEUE IMPLEMENTATION\t********************\n")
    queue = enqueueRestrictedQueue()
    while True:
        option = int(input(print("Enter your choice-:\n\t1. Insert\n\t2. Delete at start\n\t3. Delete at end\n\t4. Display\n\t5. Peek\n\t6. Refresh\n\t7. Quit\n")))
        if option == 1:
            queue.enqueueLast()
        elif option == 2:
            queue.dequeueFront()
        elif option == 3:
            queue.dequeueLast()
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
elif choice == 2:
    print("********************\tOUTPUT RESTRICTED DEQUE QUEUE IMPLEMENTATION\t********************\n")
    queue = dequeueRestrictedQueue()
    while True:
        option = int(input(print("Enter your choice:\n\t1.Insert at Start\n\t2.Insert at End\n\t3.Delete\n\t4.Display\n\t5.Peek\n\t6.Refresh\n\t7.Quit")))
        if option == 1:
            queue.enqueueFront()
        elif option == 2:
            queue.enqueueLast()
        elif option == 3:
            queue.dequeueFront()
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
else:
    print("Invalid Choice")
