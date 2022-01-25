class Node:

    def __init__(self):
        self.data = input(print("Enter data: "))
        self.next = None


class linkedStack:

    def __init__(self):
        self.start = None
        self.end = None

    def push(self):
        if self.start is None:
            node = Node()
            print("before -> start = ", self.start)
            print("before -> end = ", self.end)
            print(f"node = {node}\tvalue = {node.data}")
            self.start = node
            self.end = node
            print("after -> start = ", self.start)
            print("after -> end = ", self.end)
        else:
            node = Node()
            print("before -> start = ", self.start)
            print("before -> end = ", self.end)
            print(f"node = {node}\tvalue = {node.data}")
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            print("before -> last node = ", ptr.next)
            ptr.next = node
            self.end = node
            print("after -> start = ", self.start)
            print("after -> last node = ", ptr.next)
            print("after -> end = ", self.end)

    def pop(self):
        if self.start is None:
            print("Error: The stack is empty. Hence, pop can't be performed.")
        else:
            if self.start == self.end:
                self.start = None
                self.end = None
            else:
                ptr = self.start
                while ptr.next != self.end:
                    ptr = ptr.next
                self.end = ptr
                ptr.next = None

    def peek(self):
        if self.start is None:
            return None
        else:
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            return ptr.data

    def display(self):
        ptr = self.start
        while ptr is not None:
            print(f"{ptr}\t{ptr.data}\t{ptr.next}")
            ptr = ptr.next


stack = linkedStack()
for i in range(0, 5):
    stack.push()
    print(stack.peek())
for i in range(0, 6):
    print(f"\t {i} iteration :- ")
    stack.display()
    print(stack.peek())
    stack.pop()
