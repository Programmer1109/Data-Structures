class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


class circularQueue:

    def __init__(self):
        self.capacity = int(input(print("Enter total no. of terms: ")))
        self.leap = int(input(print("Enter the value of k: ")))
        self.start = None

    def getLength(self):
        if self.start is None:
            return 0
        else:
            count = 1
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
                count = count + 1
            return count

    def enqueue(self, val):
        if self.start is None:
            newNode = Node(val)
            self.start = newNode
            newNode.next = self.start
        else:
            newNode = Node(val)
            ptr = self.start
            while ptr.next != self.start:
                ptr = ptr.next
            ptr.next = newNode
            newNode.next = self.start

    def dequeue(self, delNode):
        ptr = self.start
        prevPtr = self.start
        while ptr.data != delNode.data:
            prevPtr = ptr
            ptr = ptr.next
        prevPtr.next = ptr.next
        return ptr.data


mainQueue = circularQueue()
mainQueue.enqueue(1)
for index in range(2, mainQueue.capacity + 1):
    mainQueue.enqueue(index)
pointer = mainQueue.start
while mainQueue.getLength() != 1:
    for index in range(1, mainQueue.leap):
        pointer = pointer.next
    print(f"Node{mainQueue.dequeue(pointer)} has been eliminated.")
print(f"node{mainQueue.start.data} is the winner")
