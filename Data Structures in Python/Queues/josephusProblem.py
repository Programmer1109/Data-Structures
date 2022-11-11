#                                                     JOSEPHUS PROBLEM IMPLMENTATION

class Node:

    def __init__(self,):
        self.data = str(input(print("Enter a value:- ")))
        self.next = None
        


print("\n************************\t\tJOSEPHUS PROBLEM IMPLMENTATION\t\t*********************\n")
capacity = int(input(print("Enter total no. of terms: ")))
leap = int(input(print("Enter the value of k: ")))
print("\nEnter elements for the Josephus Queue:- ")
balance = capacity
# Create a Josephus Queue
head = Node()
point = head
for iter in range(1, capacity):
    point.next = Node()
    point = point.next
point.next = head
point = head
print("Displaying Entered Josephus Queue:- ")
while point.next != head:
    print(f"Pointer-> {point}\t{point.data}\t{point.next}")
    point = point.next
print(f"Pointer-> {point}\t{point.data}\t{point.next}")
# Perform Josephus Elimination
pointer = head
prevPointer = None
print("\nKnockout Round...")
while balance != 1:
    count = 1
    while (count != leap):
        prevPointer = pointer
        pointer = pointer.next
        count = count + 1
    print(f"Knockout Node:- {pointer}\t{pointer.data}\t{pointer.next}")
    prevPointer.next = pointer.next
    pointer = prevPointer.next
    balance = balance - 1
print(f"\nWinner -> Survivor Node:- {prevPointer}\t{prevPointer.data}")
print("\n************************\t\tEND OF PROGRAM\t\t***************************\n")
