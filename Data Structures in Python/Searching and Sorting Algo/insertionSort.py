# Insertion SORT Algorithm
def insertionSort(List, order):
    if order == "ASC":
        for i in range(1, len(List)):
            key = List[i]
            hole = i
            while hole>0 and List[hole-1]>key:
                List[hole] = List[hole-1]
                hole -= 1
            List[hole] = key
        return List
    elif order == "DEC":
        for i in range(1, len(List)):
            key = List[i]
            hole = i
            while hole>0 and List[hole-1]<key:
                List[hole] = List[hole-1]
                hole -= 1
            List[hole] = key
        return List
    else:
        print("Error:- Invalid order entered!!!")


# Driver Code starts here
try:
    print("***************      Insertion Sort Algorithm        **************")
    List = []
    sortedList = []
    total = int(input(print("Enter total number of elements:- ")))
    for i in range(0, total):
        val = int(input(print("Enter a number:- ")))
        List.append(val)
    print(f"Unsorted List = {List}")
    val = str(input(print("Enter order to be sorted(ASC/DEC):- ")))
    print(val)
    sortedList = insertionSort(List, val)
    print(f"\nSorted List = {sortedList}")
except:
    print("Error:- Unknown!!!")
    
