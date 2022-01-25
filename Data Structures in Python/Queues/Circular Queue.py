class Queue:
    def __init__(self):
        self.capacity = 6
        self.list = [None] * self.capacity
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        print("\nInside Enqueue...")
        print("head= ", self.head)
        print("tail= ", self.tail)
        if self.head == 0 and self.tail == self.capacity - 1:
            print("Overflow Error: the list has reached its maximum capacity. Hence, insertion is not possible.")
        elif self.head == -1 and self.tail == -1:
            self.head += 1
            self.tail += 1
            self.list[self.tail] = val
        elif self.head != 0 and self.tail == self.capacity - 1:
            self.tail = 0
            self.list[self.tail] = val
        else:
            self.tail += 1
            self.list[self.tail] = val
        print(self.list)
        print("head= ", self.head)
        print("tail= ", self.tail)
        print("peek returned = ", self.peek())

    def dequeue(self):
        print("\nInside Dequeue")
        print("head= ", self.head)
        print("tail= ", self.tail)
        if self.head == -1 and self.tail == -1:
            print("Underflow Error: There is no element in the list to delete.")
        elif self.head == self.tail:
            self.list[self.head] = None
            self.head = -1
            self.tail = -1
        elif self.head == self.capacity - 1:
            self.list[self.head] = None
            self.head = 0
        else:
            self.list[self.head] = None
            self.head += 1
        print(self.list)
        print("head= ", self.head)
        print("tail= ", self.tail)
        print("peek returned = ", self.peek())

    def display(self):
        for i in range(0, self.capacity):
            print(f"list[{i}] = {self.list[i]}")

    def peek(self):
        if self.tail != -1:
            return self.list[self.head]
        else:
            return -1


queue = Queue()
roster = [12, 34, 43, 71, 65, 92]
for value in roster:
    queue.enqueue(value)
for value in range(0, 3):
    queue.dequeue()
    # print(queue.display())
queue.enqueue(39)
# print(queue.display())
queue.enqueue(19)
# print(queue.display())
queue.enqueue(29)
print(queue.display())
