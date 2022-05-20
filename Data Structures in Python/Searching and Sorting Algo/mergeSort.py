                  # Python program for implementation of MergeSort

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
