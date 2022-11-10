class Process:

    def __init__(self):
        self.processID = str(input(print("Enter Node Name:- ")))
        self.priority = int(input(print("Enter Priority No.:- ")))
        self.next = None


class priorityQueue:

    def __init__(self):
        self.start = None

    def peek(self):
        if self.start is None:
            print("Error:- Can't peek in an Empty Priority Queue")
        else:
            print("Peek Process ID = ", self.start.processID)

    def display(self):
        if self.start is None:
            print("Error: Queue is empty.")
        else:
            ptr = self.start
            print("Process\tProcess ID\tPriority\tNext Process")
            while ptr.next is not None:
                # print("Hello...")
                print(f"{ptr}   {ptr.processID}   {ptr.priority}   {ptr.next}")
                ptr = ptr.next
            print(f"{ptr}   {ptr.processID}   {ptr.priority}   {ptr.next}")

    def enqueue(self):
        newNode = Process()
        print("in enqueue...")
        print("start Node-> before = ", self.start)
        if self.start is None:
            print("Inserting in empty queue...")
            self.start = newNode
            print("start Node-> after =", self.start)
        else:
            print("Inserting Node...")
            if self.start is None or newNode.priority < self.start.priority:
                print("Inserting New Node at the Beginning...")
                print(f"Start Node:- before -> {self.start}")    
                newNode.next = self.start
                self.start = newNode
                print(f"Start Node:- after -> {self.start}")
            else:
                Ptr = self.start
                while (Ptr.next != None and Ptr.next.priority <= newNode.priority):
                    Ptr = Ptr.next
                newNode.next = Ptr.next
                Ptr.next = newNode

    def dequeue(self):
        if self.start is None:
            print("Underflow Error: The Queue is empty. Hence, pop operation can't be performed.")
        elif self.start.next is None:
            print(f"Start Node: before -> {self.start}   {self.start.processID}")
            self.start = None
            print(f"Start Node: after -> {self.start}  ")
        else:
            print(f"Start Node: before -> {self.start}   {self.start.processID}")
            self.start = self.start.next
            print(f"Start Node: after -> {self.start}   {self.start.processID}")



#                                                        PRIORITY QUEUES 
print("\n*************************\tPRIORITY QUEUE IMPLEMENTATION\t*************************\n")
print("Note:- Lower integer denotes higher priority!!!")
queue = priorityQueue()
while True:
    choice = str(input(print("Enter your choice:\n\t1. Enqueue\n\t2. Dequeue\n\t3. Peek\n\t4. Display\n\t5. Quit")))
    if choice == "1":
        queue.enqueue()
        print(queue.start)
    elif choice == "2":
        queue.dequeue()
    elif choice == "3":
        queue.peek()
    elif choice == "4":
        queue.display()
    elif choice == "5":
        exit()
    else:
        print("Inavild Choice")
print("\n*************************\t     END OF PROGRAM     \t*************************\n")
