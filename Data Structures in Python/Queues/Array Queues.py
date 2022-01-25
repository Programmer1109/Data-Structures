class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        global top
        top += 1
        self.list.append(value)
        print(self.list)
        print(self.peek())

    def dequeue(self):
        global top
        if top == -1:
            print("cannot pop from an empty queue")
        else:
            top -= 1
            del self.list[0]

    def peek(self):
        if top != -1:
            return self.list[top], self.list[0]
        else:
            return -1


queue = Queue()
top = -1
roster = [12, 34, 43, 71, 65, 92]
for value in roster:
    queue.enqueue(value)
for value in roster:
    queue.dequeue()
    print(queue.list)
    print(queue.peek())
queue.dequeue()
