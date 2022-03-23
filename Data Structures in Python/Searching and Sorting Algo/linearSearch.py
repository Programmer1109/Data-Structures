
class Node:

    def __init__(self):
        self.prev = None
        self.data = input(print("Enter data: "))
        self.next = None

    def display(self):
        print("Student id = ", self.data)


class linkedList:

    def __init__(self):
        self.start = None

    def getLength(self):
        if self.start is not None:
            count = 1
            ptr = self.start
            while ptr.next is not None:
                count = count + 1
                ptr = ptr.next
            return count
        else:
            print("Linked List is Empty")
            return 0
    
    def Insert(self, newNode):
        if self.start is not None:
            newNode = Node()
            newNode.next = None
            ptr = self.start
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = newNode
            newNode.prev = ptr
        else:
            print("Error: Node to be deleted is not present in the list.")

    def Delete(self):
        if self.start is not None:
            ptr = self.start
            prevPtr = self.start
            while ptr.next is not None:
                prevPtr = ptr
                ptr = ptr.next
            # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
            prevPtr.next = None
            # print(f"{prevPtr}\t{prevPtr.data}\t{prevPtr.next}")
        else:
            print("Error: Node to be deleted is not present in the list.")



def linearSearch(List, value):
    if len(List) >= 1:
        lengthList = len(List)
        i = 0 
        while(i != lengthList):
            if List[i] ==  value:
                return i
            else:
                continue
        if i == lengthList:
            return -1
        
    elif len(List) <= 1:
        print("Error:- List is empty!!!")


def linearSearch_LinkedList(classVar, value):
    if classVar.getLength() >= 1:
        pointer = classVar.start
        lengthList = classVar.getLength(pointer)
        index = 1
        while(index != lengthList+1):
            if pointer.data == value:
                return index
            else:
                index += 1
                pointer = pointer.next
        if index == lengthList+1:
            return -1
    elif classVar.getLength() < 1:
        print("Error:- List is empty!!!")


# Main code starts here
try:
    choice = int(input(print("Your choice:- \n\t1. Search in Array\n\t2. Search in Linked List\nEnter no. corresponding to your choice:- ")))
    if choice == 1:
        searchList = []
        totalElements = int(input(print("Enter no. of elements:- ")))
        for i in range(0, totalElements):
            searchList.append(print("Enter a number:- "))
        val = input(print("Enter the number to be searched:- "))
        flag = linearSearch(searchList, val)
        print(f"Result:-\tThe entered element was found at index {flag}.")
    elif choice == 2:
        classObject = linkedList()
        while(True):
            choice = int(input(print("Your Choice:- \n\t1. Insert in List\n\t2. Delete from List\n\t3. Stop input\nEnter no. corresponding to your choice:- ")))
            if choice == 1:
                classObject.Insert()
            elif choice == 2:
                classObject.Delete()
            elif choice == 3:
                break
        searchVal = input(print("Enter the number to be searched:- "))
        flag = linearSearch_LinkedList(classObject, searchVal)
        print(f"Result:-\tThe entered element was found at index {flag}.")
except:
    print("Error:- You have entered an invalid input!!!")
    
