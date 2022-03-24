# Implentation of Stack Data Structure using array.
class Stack:
    def __init__(self):
        self.list = []

    def push(self, value, size):
        global top
        if top == size:
            print("Overflow Error:- cannot push in an already full list.\n")
        else:
            top = top + 1
            self.list.append(value)
            print(self.list)
            print(self.peek())

    def pop(self):
        global top
        if top == -1:
            print("Underflow Error:- cannot pop from an empty stack\n")
        else:
            top = top - 1
            del self.list[-1]
            print(self.list)
            print(self.peek())

    def peek(self):
        if top != -1:
            return self.list[top]
        else:
            return -1


print("********************\t\tArray Implementation of Stacks\t\t********************\n\n")
stackList = Stack()
top = -1
total = int(input(print("Enter no. of elements:- ")))
while(True):
    choice = input(print("Choose operation to be performed:-\n\t1. Push operation\n\t2. Pop operation\n\t3. Peek operation\n\t4. Quit\nEnter your choice:- "))
    if choice == '1':
        elmentValue = int(input(print("Enter element to stack")))
        stackList.push(elmentValue, total)
    elif choice == '2':
        stackList.pop()
    elif choice == '3':
        val = stackList.peek()
        print(f"Peek = {val}")
    elif choice == '4':
        break
    else:
        print("Error:- Invalid choice of operation!!!")
print("\n\n********************\t\tEND of Program\t\t********************")
