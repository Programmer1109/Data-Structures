# Python program for implementation of MergeSort
 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def Merge(array, left, mid, right):
    # print("\nIn Merge Function:- \n")
    leftLen = mid - left + 1
    # print(f"Main Array Length = {right-left+1}")
    # print(f"Left Array Length = {leftLen}")
    rightLen = right - mid
    # print(f"Right Array Length = {rightLen}")
    leftList = [0] * leftLen
    # print(f"Left List = {leftList}")
    rightList = [0] * rightLen
    # print(f"Right List = {rightList}")

    for i in range(0, leftLen):
        # print(f"i = {i}\tleft = {left}\tmid = {mid}\tright = {right}")
        leftList[i] = array[left + i]
    for j in range(0, rightLen):
        # print(f"j = {j}\tleft = {left}\tmid = {mid}\tright = {right}")
        rightList[j] = array[mid + j + 1]

    leftIndex = 0
    rightIndex = 0
    arrayIndex = left

    while leftIndex < leftLen and rightIndex < rightLen:
        # print(f"Left Index = {leftIndex}\tRight Index = {rightIndex}\tArray Index = {arrayIndex}")
        if leftList[leftIndex] <= rightList[rightIndex]:
            array[arrayIndex] = leftList[leftIndex]
            leftIndex = leftIndex + 1
        else:
            array[arrayIndex] = rightList[rightIndex]
            rightIndex = rightIndex + 1
        arrayIndex = arrayIndex + 1

    # print(f"Left Index = {leftIndex}\tRight Index = {rightIndex}\tArray Index = {arrayIndex}")
    while leftIndex < leftLen:
        array[arrayIndex] = leftList[leftIndex]
        arrayIndex += 1
        leftIndex += 1

    while rightIndex < rightLen:
        array[arrayIndex] = rightList[rightIndex]
        arrayIndex += 1
        rightIndex += 1
    # print(array)


"""
def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
"""


def mergeSort(array, low, high):
    if low < high:
        mid = (low+high)//2

        mergeSort(array, low, mid)
        mergeSort(array, mid+1, high)
        Merge(array, low, mid, high)

 
# Driver code to test above
unsortedList = [21, 38, 29, 17, 4, 25, 32,9]
n = len(unsortedList)
print("Given array is")
for i in range(n):
    print("%d" % unsortedList[i],end=" ")
 
mergeSort(unsortedList, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % unsortedList[i],end=" ")
