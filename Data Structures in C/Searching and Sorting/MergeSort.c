#include <stdio.h>  
#include <conio.h>

void divide(int [], int , int );
void conquer(int [], int , int , int );

int main(){
    int max;
    printf("\n***************\t SELECTION SORT implementation in C LANGUAGE\t***************\n\n");
    printf("\nEnter no. of Elements:- ");
    scanf("%d", &max);
    // Accept input for Unsorted Array
    int unsortedArray[max];
    printf("Enter Elements for unsorted array:- \n");
    for (int index=0; index<max; index++){
        printf("\tEnter a No.:- ");
        scanf("%d", unsortedArray+index);
    }

    // Print the Unsorted Array
    printf("\nUnsorted Array:- ");
    for (int index=0; index<max; index++)
        printf(" %d", unsortedArray[index]);
    
    if(unsortedArray != NULL){
        // Using Selection Sort Algorithm to Sort the Array
        divide(unsortedArray, 0, max-1);
        // Printing the Sorted Array
        printf("\nSorted Array:- ");
        for (int index=0; index<max; index++)
            printf(" %d", unsortedArray[index]);
    }
    else
        printf("\nError:- EMPTY Unsorted List!!!");    getch();
    return 0;
}

void conquer(int mergeArr[], int left, int middle, int right){
    int leftLength, rightLength;
    leftLength = middle - left + 1;
    rightLength =  right - middle;
    printf("\nLength of Left = %d\tLength of Right = %d\n", leftLength, rightLength);
    int leftArray[leftLength], rightArray[rightLength];

    printf("\n");
    for(int iter = 0; iter<=leftLength-1; iter++){
        leftArray[iter] = mergeArr[left+iter];
        printf("\nleft Array[%d] = %d & merge Array[%d] = %d", iter, leftArray[iter], mergeArr[left+iter]);
    }
    for(int iter = 0; iter<=rightLength-1; iter++){
        rightArray[iter] = mergeArr[middle+iter+1];
        printf("\nright Array[%d] = %d & merge Array[%d] = %d", iter, rightArray[iter], mergeArr[middle+iter]);
    }

    int leftIndex, rightIndex, arrayIndex;
    leftIndex = 0;
    rightIndex = 0;
    arrayIndex = left;
    while(leftIndex < leftLength && rightIndex < rightIndex){
        if(leftArray[leftIndex] >= rightArray[rightIndex]){
            mergeArr[arrayIndex] = rightArray[rightIndex];
            arrayIndex++;
            rightIndex++;
        }
        else{
            mergeArr[arrayIndex] = leftArray[leftIndex];
            arrayIndex++;
            leftIndex++;
        }
    }

    while(leftIndex<leftLength){
        mergeArr[arrayIndex] = leftArray[leftIndex];
        arrayIndex++;
        leftIndex++;
    }
    while(rightIndex<rightLength){
        mergeArr[arrayIndex] = rightArray[rightIndex];
        arrayIndex++;
        rightIndex;
    }
}

void divide(int array[], int low, int high){
    int mid;
    if(low < high){
        mid = (low+high)/2;
        divide(array, low, mid);
        divide(array, mid+1, high);
        conquer(array, low, mid, high);
    }
    else 
        return;
}
