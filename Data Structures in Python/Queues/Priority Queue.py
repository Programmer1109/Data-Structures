class Node:

    def __init__(self):
        self.data = None
        self.priority = None
        self.next = None


class priorityQueue:

    def __init__(self):
        self.start = None
        self.end = None

    def peek(self):
        if self.start is None:
            print(None)
        else:
            print(self.start.data)

    def display(self):
        if self.start is None:
            print("Error: Queue is empty.")
        ptr = self.start
        while ptr.next is not None:
            print("Hello...")
            print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            ptr = ptr.next
        print(f"{ptr}\t{ptr.data}\t{ptr.next}")

    def enqueue(self):
        newNode = Node()
        newNode.data = input(print("Enter data: "))
        print("in enqueue...")
        print("start Node-> before = ", self.start)
        if self.start is None:
            print("Inserting in empty queue...")
            self.start = newNode
            print("start Node-> after =", self.start)
        else:
            print("Inserting elements...")
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode

    def dequeue(self):
        if self.start is None:
            print("Underflow Error: The Queue is empty. Hence, pop operation can't be performed.")
        else:
            self.start = self.start.next


queue = priorityQueue()
while True:
    choice = int(input(print("Enter your choice:\n\t1.Enqueue\n\t2.Dequeue\n\t3.Peek\n\t4.Display")))
    if choice == 1:
        queue.enqueue()
        print(queue.start)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.peek()
    elif choice == 4:
        queue.display()
    else:
        exit()
