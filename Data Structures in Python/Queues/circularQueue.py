
class circularQueue:
    
    def __init__(self):
        self.size = int(input(print("Enter the size of the Queue:- ")))
        self.front = -1
        self. rear = -1
        self.list = [None] * self.size

    def enqueue(self, val):
        print("\nInside Enqueue...")
        print("Front = ", self.front)
        print("Rear = ", self.rear)
        # Completely Full List
        if ((self.front == 0 and self.rear == self.size-1) or (self.front == self.rear + 1)):
            print("Overflow Error:- The Queue is Full!!!")
        # Completely EMpty List
        elif (self.front == -1 and self.rear == -1):
            self.front = self.front + 1
            self.rear += 1
            self.list[self.rear] = val
        elif (self.rear == self.size-1 and self.front != 0):
            self.rear = 0
            self.list[self.rear] = val
        # Partially filled List
        else:
            self.rear = self.rear + 1
            self.list[self.rear] = val
        print(f"Queue:- \n\tList = {self.list}\n\tHead = {self.front}\n\tRear = {self.rear}\n\tPeek Value = {self.peek}\n")

    def dequeue(self):
        print("\nInside Dequeue")
        print("Front = ", self.front)
        print("Rear = ", self.rear)
        # Completely Empty List
        if self.front == -1 and self.rear == -1:
            print("Underflow Error:- The Queue is Empty!!!")
        elif self.front == self.size-1:
            self.list[self.front] = None
            self.front = 0
        elif self.front == self.rear:
            self.list[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.list[self.front] = None
            self.front = self.front + 1
        print(f"Queue:- \n\tList = {self.list}\n\tHead = {self.front}\n\tRear = {self.rear}\n\tPeek Value = {self.peek}\n")

    def display(self):
        if self.front == 0 and self.rear < self.size:
            for i in range(0, self.rear):
                print(f"list[{i}] = {self.list[i]}")
        elif self.front != 0 and self.rear < self.size:
            for i in range(self.front, self.rear):
                print(f"list[{i}] = ", self.list[i])
        elif self.front != 0 and self.rear < self.front:
            for i in range(self.front, self.size):
                print(f"list[{i}] = ", self.list[i])
            for i in range(0, self.rear + 1):
                print(f"list[{i}] = ", self.list[i])

    def peek(self):
        if self.tail != -1:
            number = self.list[self.head]
            return number
        else:
            return -1
  


print("*****************\tCIRCULAR QUEUE IMPLEMENTATION\t*****************\n\n")
queue = circularQueue()
while True:
    choice = str(input(print("Enter your Choice:-\n\t1. Enqueue\n\t2. Dequeue\n\t3. Peek\n\t4. Display\n\t5. Quit\n")))
    if choice == '1':
        value = int(input(print("Enter an number = ")))
        queue.enqueue(value)
    elif choice == '2':
        queue.dequeue()
    elif choice == '3':
        Peek_value =  queue.peek()
        if Peek_value != -1:
            print("Peek Value = ", queue.peek())
        else:
            print("Error:- List is Full")
    elif choice == '4':
        queue.display()
    elif chooice == '5':
        break
print("\n\n*************************\t END OF PROGRAM *********************")
