#                                                     HASHMAP IMPLEMENTATION

class Node:

    def __init__(self):
        self.key = -1
        self.data = -1



class Hash_Table:
    
    def __init__(self):
        self.size = int(input(print("Enter size of Hashmap:- ")))
        self.hashArray = [None] * self.size 
        self.entries = 0
    
    def insertHashEntry(self, insert_key, insert_value):
        # Create Hash Table Element  
        hashElement = Node()
        hashElement.key = insert_key
        hashElement.data = insert_value
        # Get Hashed value of the key 
        hashIndex = self.hashFunction(insert_key)
        # If the key is not present in the Hash Table then, insert the (key, value) in the Hash Table or 
        # Else if the key is already present in Hash Table then, update the (key, value) pair.
        if self.hashArray[hashIndex] == None:
            self.hashArray[hashIndex] = hashElement
            self.entries = self.entries + 1
        else:
            self.updateHashEntry(insert_key, insert_value)

    def updateHashEntry(self, updateKey, updateValue):
        hashIndex = self.hashFunction(updateKey) 
        if self.hashArray[hashIndex] != None:
            if self.hashArray[hashIndex].key == updateKey:
                self.hashArray[hashIndex].key = updateKey
                self.hashArray[hashIndex].data = updateValue
                return
            else:
                print("Error:- Update is not Possible, no such Key found in Hash Table !!!")
        else:            
            print("Error:- Update is not Possible, no element found at given address !!!")
        
    def searchHashEntry(self, searchKey):
        # print(f"Search Key = {searchKey}")
        hashIndex = self.hashFunction(searchKey)
        # print(f"Hash Index = {hashIndex}")
        if self.hashArray[hashIndex] != None:
            # print("hash element key = ", self.hashArray[hashIndex].key)
            if self.hashArray[hashIndex].key == searchKey:
                hashElement = [hashIndex, self.hashArray[hashIndex].key, self.hashArray[hashIndex].data]
                # print(f"Hash Element = {hashElement}")
                return hashElement
            else:
                return None
        else:
            return None

    def deleteHashEntry(self, deleteKey):
        hashIndex = self.hashFunction(deleteKey)
        if self.hashArray[hashIndex] != None:
            if self.hashArray[hashIndex].key == deleteKey:
                self.hashArray[hashIndex].key = -1
                self.hashArray[hashIndex].data = -1
                self.hashArray[hashIndex] = None
                self.entries = self.entries - 1
            else:
                print("Error:- No such Key exists in the Hash Table!!!")
        else:
            print("Error:- No such Key exists in the Hash Table!!!")
        
    def displayHashTable(self):      
        if self.entries != 0:
            index = 0
            while index != self.size:
                if self.hashArray[index] != None:
                    print(f"Index = {index}\tKey = {self.hashArray[index].key}\tData = {self.hashArray[index].data}")
                index = index + 1
        else:
            print("Error:- the Hash Table is Empty!!!")

    def hashFunction(self, index):
        return index%self.size



#   MAIN CODE STARTS HERE
print("\n*************************\tHASHMAP IMPLEMENTATION IN PYTHON\t*************************\n")
Hashmap = Hash_Table()
while True:
    choice = int(input(print("\nChoose your operation:-\n\t1. Insert Hash Entry\n\t2. Update Hash Entry\n\t3. Delete from Hash Table\n\t4. Search in Hash Table\n\t5. Display Hash Entries\n\t6. Quit\nEnter your choice:- ")))
    if choice == 1:
        userKey = int(input(print("Enter the value of key:- ")))
        userData = str(input(print("Enter the data for Key to be Inserted or Updated:- ")))
        Hashmap.insertHashEntry(userKey, userData)
    elif choice == 2:
        userKey = int(input(print("Enter the value of key:- ")))
        userData = str(input(print("Enter the data to be Updated:- ")))
        Hashmap.updateHashEntry(userKey, userData)
    elif choice == 3:
        userKey = int(input(print("Enter the value of key:- ")))
        Hashmap.deleteHashEntry(userKey)
    elif choice == 4:
        userKey = int(input(print("Enter the value of key:- ")))
        searchResult = Hashmap.searchHashEntry(userKey)
        if searchResult != None:
            print(f"Search Results:-\tIndex = {searchResult[0]}\tKey = {searchResult[1]}\tData = {searchResult[2]}\n")
        else:
            print("Error:- Search Returned Nothing!!!")
    elif choice == 5:
        Hashmap.displayHashTable()
    elif choice == 6:
        break
    else:
        print("Invalid Choice!!!")
print("\n********************************\tEND OF PROGRAM\t********************************\n")
