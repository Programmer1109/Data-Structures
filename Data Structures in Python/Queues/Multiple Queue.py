class multipleQueue:

    def __init__(self):
        self.capacity = int(input(print("Enter size of queue: ")))
        self.list = [None] * self.capacity
        self.headA = -1
        self.tailA = -1
        self.headB = self.capacity
        self.tailB = self.capacity

    def refresh(self):
        for index in range(self.capacity):
            self.list[index] = None
        self.headA = -1
        self.tailA = -1
        self.headB = self.capacity
        self.tailB = self.capacity

    def enqueueA(self, value):
        if self.tailA == self.tailB - 1:
            print("Overflow Error: the queue is full. Hence, unable to insert element")
        elif self.headA == -1 and self.tailA == -1:
            self.headA = 0
            self.tailA = 0
            self.list[self.tailA] = value
        else:
            self.tailA += 1
            self.list[self.tailA] = value

    def dequeueA(self):
        if self.headA == -1 or self.headA == self.tailB:
            print("Underflow Error: can't delete from an empty queue")
        else:
            self.list[self.headA] = None
            self.headA += 1
            print("head queueA -> ", self.headA)
            print("tail queueA -> ", self.tailA)
            print("head queueB -> ", self.headB)
            print("tail queueB -> ", self.tailB)

    def displayA(self):
        if self.headA == -1:
            print("Error: No elements to display empty queue.")
        else:
            index = self.headA
            while index != self.tailA + 1:
                print(f"list[{index}] = {self.list[index]}")
                index = index + 1
                print(index)
            print(self.list)

    def enqueueB(self, value):
        if self.tailA == self.tailB - 1:
            print("Overflow Error: the queue is full. Hence, unable to insert element")
        elif self.headB == self.capacity and self.tailB == self.capacity:
            self.headB = self.capacity - 1
            self.tailB = self.capacity - 1
            self.list[self.tailB] = value
        else:
            self.tailB -= 1
            self.list[self.tailB] = value

    def dequeueB(self):
        if self.headB == self.capacity or self.headB == self.tailA:
            print("Underflow Error: can't delete from an empty queue")
        else:
            self.list[self.headB] = None
            self.headB -= 1
            print("head queueA -> ", self.headA)
            print("tail queueA -> ", self.tailA)
            print("head queueB -> ", self.headB)
            print("tail queueB -> ", self.tailB)

    def displayB(self):
        if self.headB == self.capacity:
            print("Error: No elements to display empty queue.")
        else:
            index = self.headB
            while index != self.tailB - 1:
                print(f"list[{index}] = {self.list[index]}")
                index = index - 1
                print(index)
            print(self.list)


queue = multipleQueue()
while True:
    choice = int(input(print("Enter your choice:-\n\t1.Insert in QueueA\n\t2.Insert in QueueB\n\t3.Delete in QueueA\n\t"
                             "4.Delete in QueueB\n\t5.Display QueueA\n\t6.Display QueueB\n\t7.Reresh\n\t8.Exit\n")))
    if choice == 1:
        val = input(print("Enter data: "))
        queue.enqueueA(val)
    elif choice == 2:
        val = input(print("Enter data: "))
        queue.enqueueB(val)
    elif choice == 3:
        queue.dequeueA()
    elif choice == 4:
        queue.dequeueB()
    elif choice == 5:
        queue.displayA()
    elif choice == 6:
        queue.displayB()
    elif choice == 7:
        queue.refresh()
    elif choice == 8:
        exit()
    else:
        print("Error: Invalid choice")
