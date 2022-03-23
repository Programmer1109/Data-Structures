
def selectionSort(List, order):
    if order == "ASC":
        for i in range(0, len(List)-1):
            min = List[i]
            index = i
            for j in range(i+1, len(List)):
                if List[j] < min:
                    min = List[j]
                    index = j
                j = j + 1 
            print(f"Minimum :-\t index = {index}\t elem = {List[index]}")
            temp = List[i]
            List[i] = List[index]
            List[index] = temp
            print(List)
            print("\n")
        return List
    elif order == "DEC":
        for i in range(0, len(List)-1):
            max = List[i]
            index = i
            for j in range(i+1, len(List)):
                if List[j] > max:
                    max = List[j]
                    index = j
                j = j + 1 
            print(f"Minimum :-\t index = {index}\t elem = {List[index]}")
            temp = List[i]
            List[i] = List[index]
            List[index] = temp
            print(List)
            print("\n")
        return List
    else:
        print("Error:- Invalid order entered!!!")


# Driver Code starts here
try:
    print("***************      Selection Sort Algorithm        **************")
    List = []
    sortedList = []
    total = int(input(print("Enter total number of elements:- ")))
    for i in range(0, total):
        val = int(input(print("Enter a number:- ")))
        List.append(val)
    print(f"Unsorted List = {List}")
    val = str(input(print("Enter order to be sorted(ASC/DEC):- ")))
    print(val)
    sortedList = selectionSort(List)
    print(f"Sorted List = {sortedList}")
except:
    print("Error:- Unknown!!!")
    
