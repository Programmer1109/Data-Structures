#                                              IMPLEMENTATION of BINARY HEAPS

class binaryMaxHeap:

    def __init__(self):
        self.totalElements = 0
        self.binaryMaxHeapArray = []
        self.binaryMaxHeapArray.append(None)

    def insert_max_heap(self, newElement):
        print(f"Before ->\nTotal Elements = {self.totalElements}\tBinary Max Heap = {self.binaryMaxHeapArray}")
        self.totalElements = self.totalElements + 1
        self.binaryMaxHeapArray.append(newElement)
        position = self.totalElements
        print(f"After ->\nTotal Elements = {self.totalElements}\tBinary Max Heap = {self.binaryMaxHeapArray}\nPosition = {position}")
        print("\nEnter the Loop...")
        while position > 1:
            parent = position // 2
            print(f"\tParent Index = {parent}\tPosition = {position}")
            if self.binaryMaxHeapArray[parent] >= self.binaryMaxHeapArray[position]:
                print("NOTE:- Everything's fine...")
                break
            else:
                # Swap the Parent Node with the newly introduced Child Node 
                print("NOTE:- Performing Swap...")
                print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tChild Value = {self.binaryMaxHeapArray[position]}")
                temporary = self.binaryMaxHeapArray[parent]
                self.binaryMaxHeapArray[parent] = self.binaryMaxHeapArray[position]
                self.binaryMaxHeapArray[position] = temporary
                print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tChild Value = {self.binaryMaxHeapArray[position]}")
                position = parent               

    def delete_max_heap(self):
        print("Deleting from the BINARY MAX HEAP")
        print("Old Heap :- ", self.binaryMaxHeapArray)
        print(f"Before -> Start Element = {self.binaryMaxHeapArray[1]}\tLast Element = {self.binaryMaxHeapArray[self.totalElements]}\tNumber of Elements = {self.totalElements}")
        # SWAP the FIRST Element as the LAST Element
        rootValue = self.binaryMaxHeapArray[1]
        self.binaryMaxHeapArray[1] = self.binaryMaxHeapArray[self.totalElements]
        self.binaryMaxHeapArray[self.totalElements] = rootValue
        # Reduce no. of elements
        self.totalElements = self.totalElements - 1
        print(f"After -> Start Element = {self.binaryMaxHeapArray[1]}\tLast Element = {self.binaryMaxHeapArray[self.totalElements]}\tNumber of Elements = {self.totalElements}")
        parent = 1
        leftChild = 2
        rightChild = 3
        while leftChild <= self.totalElements:
            if leftChild != self.totalElements:
                print(f"\nIn IF leftChild == N, Before -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                if self.binaryMaxHeapArray[parent] >= self.binaryMaxHeapArray[leftChild] and self.binaryMaxHeapArray[parent] >= self.binaryMaxHeapArray[rightChild]:
                    print("PARENT node value is greater than LEFT CHILD and RIGHT CHILD...")
                    print("NOTE:- Everything's Fine!!! ")
                    break
                elif self.binaryMaxHeapArray[parent] <= self.binaryMaxHeapArray[leftChild] and self.binaryMaxHeapArray[parent] >= self.binaryMaxHeapArray[rightChild]:
                    # SWAP the node pointed out by PARENT with LEFTCHILD
                    print("PARENT node value is lesser than LEFT CHILD but greater RIGHT CHILD...") 
                    print("Swapping the PARENT node with it's LEFT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tLeft Child Value = {self.binaryMaxHeapArray[leftChild]}")
                    temporary = self.binaryMaxHeapArray[leftChild]
                    self.binaryMaxHeapArray[leftChild] = self.binaryMaxHeapArray[parent]
                    self.binaryMaxHeapArray[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tChild Value = {self.binaryMaxHeapArray[leftChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                    parent = leftChild
                elif self.binaryMaxHeapArray[parent] >= self.binaryMaxHeapArray[leftChild] and self.binaryMaxHeapArray[parent] <= self.binaryMaxHeapArray[rightChild]:
                    # SWAP  the node pointed out by PARENT with RIGHTCHILD
                    print("PARENT node value is greater than LEFT CHILD but lesser RIGHT CHILD...")
                    print("Swapping the PARENT node with it's RIGHT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tRight Child Value = {self.binaryMaxHeapArray[rightChild]}")
                    temporary = self.binaryMaxHeapArray[rightChild]
                    self.binaryMaxHeapArray[rightChild] = self.binaryMaxHeapArray[parent]
                    self.binaryMaxHeapArray[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tRight Child Value = {self.binaryMaxHeapArray[rightChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                    parent = rightChild
                elif self.binaryMaxHeapArray[parent] <= self.binaryMaxHeapArray[leftChild] and self.binaryMaxHeapArray[parent] <= self.binaryMaxHeapArray[rightChild]:
                    print("PARENT node value is lesser than LEFT CHILD and RIGHT CHILD...")
                    if self.binaryMaxHeapArray[leftChild] >= self.binaryMaxHeapArray[rightChild]:
                        # SWAP the node pointed out by PARENT with LEFTCHILD 
                        print("Swapping the PARENT node with it's LEFT child node...")
                        print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tLeft Child Value = {self.binaryMaxHeapArray[leftChild]}")
                        temporary = self.binaryMaxHeapArray[leftChild]
                        self.binaryMaxHeapArray[leftChild] = self.binaryMaxHeapArray[parent]
                        self.binaryMaxHeapArray[parent] = temporary
                        print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tChild Value = {self.binaryMaxHeapArray[leftChild]}")
                        print(f"After -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                        parent = leftChild
                    else:
                        # SWAP  the node pointed out by PARENT with RIGHTCHILD
                        print("Swapping the PARENT node with it's RIGHT child node...")
                        print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tRight Child Value = {self.binaryMaxHeapArray[rightChild]}")
                        temporary = self.binaryMaxHeapArray[rightChild]
                        self.binaryMaxHeapArray[rightChild] = self.binaryMaxHeapArray[parent]
                        self.binaryMaxHeapArray[parent] = temporary
                        print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tRight Child Value = {self.binaryMaxHeapArray[rightChild]}")
                        print(f"After -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                        parent = rightChild
            else:
                print(f"\nIn ELSE, Before -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMaxHeapArray[rightChild]}")
                if self.binaryMaxHeapArray[leftChild] > self.binaryMaxHeapArray[parent]:
                    # SWAP the node pointed out by PARENT with LEFTCHILD
                    print("PARENT node value is lesser than LEFT CHILD but greater RIGHT CHILD...") 
                    print("Swapping the PARENT node with it's LEFT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tLeft Child Value = {self.binaryMaxHeapArray[leftChild]}")
                    temporary = self.binaryMaxHeapArray[leftChild]
                    self.binaryMaxHeapArray[leftChild] = self.binaryMaxHeapArray[parent]
                    self.binaryMaxHeapArray[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMaxHeapArray[parent]}\tChild Value = {self.binaryMaxHeapArray[leftChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMaxHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMaxHeapArray[leftChild]}")
                    parent = leftChild
                else:
                    parent = leftChild
            leftChild = 2 * parent
            rightChild = 2 * parent + 1
            print(f"values for next iteration,\n\tParent = {parent}\tLeft Child = {leftChild}\tRight Child = {rightChild}")
        print("New Heap :- ", self.binaryMaxHeapArray)

    def search_max_heap(self, searchKey):
        if self.totalElements > 1:
            for index in range(1, self.totalElements+1):
                if searchKey == self.binaryMaxHeapArray[index]:
                    return index
            return -1
        elif self.totalElements == 1:
            if self.binaryMaxHeapArray[1] == searchKey:
                return 1
            else:
                return -1
        else:
            return -1
    
    def minimum_element(self):
        if self.totalElements >= 1:
            minimumElement = self.binaryMaxHeapArray[1]
            print(f"Minimum Element = {minimumElement}\t")
            for index in range(2, self.totalElements+1):
                print(f"Index = {index}")
                if self.binaryMaxHeapArray[index] < minimumElement:
                    minimumElement = self.binaryMaxHeapArray[index]
                print(f"Minimum Element = {minimumElement}")
            return minimumElement
        else:
            return -1



class binaryMinHeap:

    def __init__(self):
        self.totalElements = 0
        self.binaryMinHeapArray = []
        self.binaryMinHeapArray.append(None)

    def insert_min_heap(self, newElement):
        print(f"Before ->\nTotal Elements = {self.totalElements}\tBinary Max Heap = {self.binaryMinHeapArray}")
        self.totalElements = self.totalElements + 1
        self.binaryMinHeapArray.append(newElement)
        position = self.totalElements
        print(f"After ->\nTotal Elements = {self.totalElements}\tBinary Max Heap = {self.binaryMinHeapArray}\nPosition = {position}")
        print("\nEnter the Loop...")
        while position > 1:
            parent = position // 2
            print(f"\tParent Index = {parent}\tPosition = {position}")
            if self.binaryMinHeapArray[parent] <= self.binaryMinHeapArray[position]:
                print("NOTE:- Everything's fine...")
                break
            else:
                # Swap the Parent Node with the newly introduced Child Node 
                print("NOTE:- Performing Swap...")
                print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tChild Value = {self.binaryMinHeapArray[position]}")
                temporary = self.binaryMaxHeapArray[parent]
                self.binaryMaxHeapArray[parent] = self.binaryMaxHeapArray[position]
                self.binaryMaxHeapArray[position] = temporary
                print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tChild Value = {self.binaryMinHeapArray[position]}")
                position = parent
    
    def delete_min_heap(self):
        print("Deleting from the BINARY MIN HEAP")
        print("Old Heap :- ", self.binaryMinHeapArray)
        print(f"Before -> Start Element = {self.binaryMinHeapArray[1]}\tLast Element = {self.binaryMinHeapArray[self.totalElements]}\tNumber of Elements = {self.totalElements}")
        # Set the FIRST Element as the LAST Element
        rootValue = self.binaryMinHeapArray[1]
        self.binaryMinHeapArray[1] = self.binaryMinHeapArray[self.totalElements]
        self.binaryMinHeapArray[self.totalElements] = rootValue
        # Deduct no. of elements
        self.totalElements = self.totalElements - 1
        print(f"After -> Start Element = {self.binaryMinHeapArray[1]}\tLast Element = {self.binaryMinHeapArray[self.totalElements]}\tNumber of Elements = {self.totalElements}")
        parent = 1
        leftChild = 2
        rightChild = 3
        while leftChild <= self.totalElements:
            if leftChild != self.totalElements:
                print(f"\nBefore -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMinHeapArray[rightChild]}")
                if self.binaryMinHeapArray[parent] <= self.binaryMinHeapArray[leftChild] and self.binaryMinHeapArray[parent] <= self.binaryMinHeapArray[rightChild]:
                    print("NOTE:- Everything's Fine!!! ")
                    break
                elif self.binaryMinHeapArray[parent] >= self.binaryMinHeapArray[leftChild] and self.binaryMinHeapArray[parent] <= self.binaryMinHeapArray[rightChild]:
                    # SWAP the node pointed out by PARENT with LEFTCHILD 
                    print("Swapping the PARENT node with it's LEFT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tLeft Child Value = {self.binaryMinHeapArray[leftChild]}")
                    temporary = self.binaryMinHeapArray[leftChild]
                    self.binaryMinHeapArray[leftChild] = self.binaryMinHeapArray[parent]
                    self.binaryMinHeapArray[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tChild Value = {self.binaryMinHeapArray[leftChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMinHeapArray[rightChild]}")
                    parent = leftChild
                elif self.binaryMinHeapArray[parent] <= self.binaryMinHeapArray[leftChild] and self.binaryMinHeapArray[parent] >= self.binaryMinHeapArray[rightChild]:
                    # SWAP  the node pointed out by PARENT with RIGHTCHILD
                    print("Swapping the PARENT node with it's RIGHT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tRight Child Value = {self.binaryMinHeapArray[rightChild]}")
                    temporary = self.binaryMinHeapArray[rightChild]
                    self.binaryMinHeapArray[rightChild] = self.binaryMinHeapArray[parent]
                    self.binaryMinHeapArrayparent[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tRight Child Value = {self.binaryMinHeapArray[rightChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMinHeapArray[rightChild]}")
                    parent = rightChild
                elif self.binaryMinHeapArray[parent] >= self.binaryMinHeapArray[leftChild] and self.binaryMinHeapArray[parent] >= self.binaryMinHeapArray[rightChild]:
                    print("PARENT node value is greater than LEFT CHILD and RIGHT CHILD...")
                    if self.binaryMinHeapArray[leftChild] <= self.binaryMinHeapArray[rightChild]:
                        # SWAP the node pointed out by PARENT with LEFTCHILD 
                        print("Swapping the PARENT node with it's LEFT child node...")
                        print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tLeft Child Value = {self.binaryMinHeapArray[leftChild]}")
                        temporary = self.binaryMinHeapArray[leftChild]
                        self.binaryMinHeapArray[leftChild] = self.binaryMinHeapArray[parent]
                        self.binaryMinHeapArray[parent] = temporary
                        print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tChild Value = {self.binaryMinHeapArray[leftChild]}")
                        print(f"After -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMinHeapArray[rightChild]}")
                        parent = leftChild
                    else:
                        # SWAP  the node pointed out by PARENT with RIGHTCHILD
                        print("Swapping the PARENT node with it's RIGHT child node...")
                        print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tRight Child Value = {self.binaryMinHeapArray[rightChild]}")
                        temporary = self.binaryMinHeapArray[rightChild]
                        self.binaryMinHeapArray[rightChild] = self.binaryMinHeapArray[parent]
                        self.binaryMinHeapArrayparent[parent] = temporary
                        print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tRight Child Value = {self.binaryMinHeapArray[rightChild]}")
                        print(f"After -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}\t Right Child @ {rightChild} = {self.binaryMinHeapArray[rightChild]}")
                        parent = rightChild
            else:
                if self.binaryMinHeapArray[leftChild] < self.binaryMinHeapArray[parent]:
                    # SWAP the node pointed out by PARENT with LEFTCHILD 
                    print("Swapping the PARENT node with it's LEFT child node...")
                    print(f"Before Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tLeft Child Value = {self.binaryMinHeapArray[leftChild]}")
                    temporary = self.binaryMinHeapArray[leftChild]
                    self.binaryMinHeapArray[leftChild] = self.binaryMinHeapArray[parent]
                    self.binaryMinHeapArray[parent] = temporary
                    print(f"After Swap:-\tParent Value = {self.binaryMinHeapArray[parent]}\tChild Value = {self.binaryMinHeapArray[leftChild]}")
                    print(f"After -> Parent Element @ {parent} = {self.binaryMinHeapArray[parent]}\tLeft Child @ {leftChild} = {self.binaryMinHeapArray[leftChild]}")
                    parent = leftChild
                else:
                    parent = leftChild
            leftChild = 2 * parent
            rightChild = 2 * parent + 1
        print("New Heap :- ", self.binaryMinHeapArray)

    def search_min_heap(self, searchKey):
        if self.totalElements > 1:
            for index in range(1, self.totalElements+1):
                if searchKey == self.binaryMinHeapArray[index]:
                    return index
            return -1
        elif self.totalElements == 1:
            if self.binaryMinHeapArray[1] == searchKey:
                return 1
            else:
                return -1
        else:
            return -1

    def maximum_element(self):
        if self.totalElements >= 1:
            maximumElement = self.binaryMinHeapArray[1]
            for index in range(2, self.totalElements+1):
                if self.binaryMinHeapArray[index] > maximumElement:
                    maximumElement = self.binaryMinHeapArray[i]
            return maximumElement
        else:
            return -1




def displayHeap(heapArray, heapSize):
    if heapSize <= 0:
        print("Error:- Can't display EMPTY Heap!!!")
    else:
        for index in range(1, heapSize+1):
            print(f"Heap Element @ {index} = {heapArray[index]}")

    
#                                                  MAIN CODE STARTS HERE
print("\n*************************\tBINARY HEAP IMPLEMENTATION IN PYTHON\t*************************\n")
maxHeap = binaryMaxHeap()
minHeap = binaryMinHeap()
maxHeapORminHeap = str(input(print("Choose from the following:-\n\t1. Perform operations on Max Heap\n\t2. Perform operations on Min Heap\nEnter Your Choice:- ")))
if maxHeapORminHeap.lower() == "max" or maxHeapORminHeap == "1" or maxHeapORminHeap.lower() == "max heap":
    while True:
        choice = str(input(print("\nChoose your operation:-\n\t1. Insert in Max Heap\n\t2. Delete from Max Heap\n\t3. Search in Max Heap\n\t4. Display Nodes in Max Heap\n\t5. Find Smallest Node\n\t6.Quit\nEnter your choice:- ")))
        if choice == "1":
            keyValue = int(input(print("Enter the value of key:- ")))
            maxHeap.insert_max_heap(keyValue)
        elif choice == "2":
            maxHeap.delete_max_heap()
        elif choice == "3":
            keyValue = int(input(print("Enter the value of key:- ")))
            searchResult = maxHeap.search_max_heap(keyValue)
            if searchResult != -1:
                print(f"Search Results:-  Element found at {searchResult} = {maxHeap.binaryMaxHeapArray[searchResult]}")
            else:
                print(f"Search Results:-  Error -> Can't find mimimum element in an EMPTY HEAP!!!")
        elif choice == "4":
            displayHeap(maxHeap.binaryMaxHeapArray, maxHeap.totalElements)
        elif choice == "5":
            minValue = maxHeap.minimum_element()
            if minValue != -1:
                print(f"Results:- Minimum Element Value = {minValue}")
            else:
                print(f"Results:- No Minimum Element in an EMPTY Heap!!!")
        elif choice == "6":
            break
        else:
            print("Error:- Invalid Choice!!! Please Enter a Valid Choice.")
elif maxHeapORminHeap.lower() == "min" or maxHeapORminHeap == "2" or maxHeapORminHeap.lower() == "min heap":
    while True:
        choice = str(input(print("\nChoose your operation:-\n\t1. Insert in Min Heap\n\t2. Delete from Min Heap\n\t3. Search in Min Heap\n\t4. Display Nodes in Max Heap\n\t5. Find Largest Element\n\t6. Quit\nEnter your choice:- ")))
        if choice == "1":
            keyValue = int(input(print("Enter the value of key:- ")))
            minHeap.insert_min_heap(keyValue)
        elif choice == "2":
            keyValue = int(input(print("Enter the value of key:- ")))
            minHeap.delete_min_heap(keyValue)
        elif choice == "3":
            keyValue = int(input(print("Enter the value of key:- ")))
            searchResult = minHeap.search_min_heap(keyValue)
            if searchResult != -1:
                print(f"Search Results:-  Element found at {searchResult} = {maxHeap.binaryMinHeapArray[searchResult]}")
            else:
                print(f"Search Results:-  Error -> Can't find mimimum element in an EMPTY HEAP!!!")
        elif choice == "4":
            displayHeap(minHeap.binaryMinHeapArray, minHeap.totalElements)
        elif choice == "5":
            maxValue = minHeap.maximum_element()
            if maxValue == -1:
                print(f"Results:- Minimum Element Value = {maxValue}")
            else:
                print(f"Results:- No Maximum Element in an EMPTY Heap!!!")
        elif choice == "6":
            break
        else:
            print("Error:- Invalid Choice!!! Please Enter a Valid Choice.")
else:
    print("Error:- Invalid Choice!!! Please Enter a Valid Choice.")
print("\n********************************\tEND OF PROGRAM\t********************************\n")
