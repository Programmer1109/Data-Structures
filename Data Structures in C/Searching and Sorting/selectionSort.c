#include<stdio.h>
#include <conio.h>

int* selectionSort(int [], int );

int main(){
    int max;
    printf("\n***************\t SELECTION SORT implementation in C LANGUAGE\t***************\n\n");
    printf("\nEnter no. of Elements:- ");
    scanf("%d", &max);
    // Accept input for Unsorted Array
    int unsortedArray[max];
    int* sortedArray;
    printf("Enter Elements for unsorted array:- \n");
    for (int index=0; index<max; index++){
        printf("\tEnter a No.:- ");
        scanf("%d", unsortedArray+index);
    }

    // Print the Unsorted Array
    printf("\nUnsorted Array:- ");
    for (int index=0; index<max; index++)
        printf(" %d", unsortedArray[index]);
    
    // Using Selection Sort Algorithm to Sort the Array
    sortedArray = selectionSort(unsortedArray, max);

    // Printing the Sorted Array
    if(sortedArray != NULL){
        printf("\nSorted Array:- ");
        for (int index=0; index<max; index++)
            printf(" %d", *(sortedArray+index));
    }
    else
        printf("\nError:- EMPTY Unsorted List!!!");

    getch();
    return 0;
}

int* selectionSort(int array[], int length){
    if (length >= 2){
        int min;
        int temp;
        for (int i = 0; i<length-1; i++){
            min = i;
            for (int j=i+1; j<=length-1; j++){
                if (array[j] < array[min])
                    min = j;
                else
                    continue;
            }
            temp = array[min];
            array[min] = array[i];
            array[i] = temp;
        }
        return array;
    }
    else if (length == 1)
        return array;
    else 
        return NULL;
}

