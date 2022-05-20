                        # Quick Sort Algorithm Python Implementstion


def partition(array, low, high):
    pivot = array[low]
    end = high
    start = low+1

    while start <= end:
        if pivot <= array[start]:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp
            end = end - 1
            start = start + 1
    temp = array[low]
    array[low] = array[start]
    array[start] = temp

    return start


def quickSort(array, low, high):
    if low < high:
        partitionIndex = partition(array, low, high)
        quickSort(array, low, partitionIndex)
        quickSort(array, partitionIndex+1, high)
    else:
        return
 
 
unsortedList = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(unsortedList)
 
example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]
result = [1, 2, 2, 4, 4, 5, 6, 6, 7, 8]
# As you can see, it works for duplicates too
print(quickSort(0, len(example)-1, example))
