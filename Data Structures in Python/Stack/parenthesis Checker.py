class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        global top
        # print("in push before -> top  = ", top)
        top += 1
        # print("in push after -> top  = ", top)
        self.list.append(value)
        print(self.peek())

    def pop(self, current):
        global top
        # print("in pop before -> top  = ", top)
        if top == -1:
            print("cannot pop from an empty stack")
        else:
            if self.list[top] == '(' and current == ')':
                del self.list[-1]
            elif self.list[top] == '[' and current == ']':
                del self.list[-1]
            elif self.list[top] == '{' and current == '}':
                del self.list[-1]
            top -= 1
            # print("in pop after -> top  = ", top)

    def peek(self):
        if top != -1:
            return self.list[top]
        else:
            return -1


stack = Stack()
top = -1
sequence = input(print("Enter a sequence of parenthesis: "))
for index in range(len(sequence)):
    if sequence[index] == '(' or sequence[index] == '[' or sequence[index] == '{':
        stack.push(sequence[index])
    elif sequence[index] == ')' or sequence[index] == ']' or sequence[index] == '}':
        stack.pop(sequence[index])

if top == -1:
    print("Balanced")
else:
    print("Unbalanced")
