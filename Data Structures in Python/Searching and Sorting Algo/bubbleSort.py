# Bubble Sort Algorithm 
def bubbleSort(List, order):
    if order == "ASC":
        for i in range(0, len(List)):
            for j in range(0, len(List)-1):
                if List[j] > List[j+1]:
                    temp = List[j]
                    List[j] = List[j+1]
                    List[j+1] = temp
                else:
                    continue
        return List
    elif order == "DEC":
        for i in range(0, len(List)):
            for j in range(0, len(List)-1):
                if List[j] < List[j+1]:
                    temp = List[j]
                    List[j] = List[j+1]
                    List[j+1] = temp
                else:
                    continue
        return List
    else:
        print("Error:- Invalid order entered!!!")


try:
    print("*******************      Bubble Sort Algorithm        ************************")
    searchList = []
    totalElements = int(input(print("Enter no. of elements:- ")))
    for i in range(0, totalElements):
        value = int(input(print("Enter a number:- ")))
        searchList.append(value)
    print(f"Unordered List = {searchList}")
    val = str(input(print("Enter order to be sorted(ASC/DEC):- ")))
    print(val)
    sortedList = bubbleSort(searchList, val)
    print(f"Result:-\tThe entered element was found at index {sortedList}.")
except:
    print("Error:- You have entered an invalid input!!!")
