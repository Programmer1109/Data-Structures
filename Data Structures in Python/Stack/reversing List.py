class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        global top
        top += 1
        self.list.append(value)
        print(self.list)
        print(self.peek())

    def pop(self):
        global top, revList
        if top == -1:
            print("cannot pop from an empty stack")
        else:
            top -= 1
            revList.append(self.list[-1])
            del self.list[-1]

    def peek(self):
        if top != -1:
            return self.list[top]
        else:
            return -1


stack = Stack()
top = -1
roster = [12, 34, 43, 71, 65, 92]
revList = []
for value in roster:
    stack.push(value)
for value in roster:
    stack.pop()
    print(stack.list)
    print(stack.peek())
stack.pop()
print(revList)
