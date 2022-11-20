#                                                 MAXIMUM FREQUENCY OF ELEMENTS

class Node:

    def __init__(self):
        self.key = -1
        self.frequency = 0



class Hash_Table:
    
    def __init__(self, length):
        self.size = length
        self.hashArray = [None] * self.size 
        self.entries = 0
    
    def insertHashEntry(self, insert_key, insert_value):
        # Get Hashed value of the key 
        hashIndex = self.hashFunction(insert_key)
        # If the key is not present in the Hash Table then, insert the (key, value) in the Hash Table or 
        # Else if the key is already present in Hash Table then, update the (key, value) pair.
        if self.hashArray[hashIndex] == None:
            # Create Hash Table Element  
            hashElement = Node()
            hashElement.key = insert_key
            self.hashArray[hashIndex] = hashElement
            self.hashArray[hashIndex].frequency = self.hashArray[hashIndex].frequency + 1
            self.entries = self.entries + 1
        elif self.hashArray[hashIndex].key == insert_key:
            self.hashArray[hashIndex].frequency = self.hashArray[hashIndex].frequency + 1

    def hashFunction(self, index):
        return index%self.size



#               MAIN CODE STARTS HERE
inputArray = []
arraySize = int(input(print("Enter the size of Array:- ")))
for index in range(0, arraySize):
    element = int(input(print("Enter value of element = ")))
    inputArray.append(element)
# Create a Hash Table with the Array Elements
Hashmap = Hash_Table(arraySize)
for value in inputArray:
    Hashmap.insertHashEntry(value)
# Search for most frequent value
mostFrequent = 0
mostFrequentKey = inputArray[0]
index = 0 
while index != arraySize:
    if Hashmap.hashArray[index] != None:
        if Hashmap.hashArray[index].frequency > mostFrequent:
            mostFrequent = Hashmap.hashArray[index].frequency
            mostFrequentKey = Hashmap.hashArray[index].key
        else:
            index += 1
    else:
        index += 1
print(f"Solution:-\n\tElement Value = {mostFrequentKey}\tElement Frequency = {mostFrequent}")
