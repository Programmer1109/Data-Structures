class Node:

    def __init__(self):
        self.data = input(print("Enter data: "))
        self.next = None


class linkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        if self.front is None:
            node = Node()
            self.front = node
            self.rear = node
        else:
            node = Node()
            ptr = self.front
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            print("Underflow Error: The Queue is empty. Hence, pop operation can't be performed.")
        else:
            self.front = self.front.next

    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data

    def display(self):
        ptr = self.front
        if ptr is None:
            print("Underflow Error: The Queue is empty.")
        while ptr is not None:
            print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            ptr = ptr.next


queue = linkedQueue()
for i in range(0, 5):
    queue.display()
    queue.enqueue()
    print(queue.peek())
for i in range(0, 6):
    print(f"\t {i} iteration :- ")
    queue.display()
    queue.dequeue()
    print(queue.peek())
