#include<stdio.h>
#include <conio.h>

int* insertionSort(int [], int );

int main(){
    int max;
    printf("\n***************\t INSERTION SORT implementation in C LANGUAGE\t***************\n\n");
    printf("Enter no. of Elements:- ");
    scanf("%d", &max);
    // Accept input for Unsorted Array
    int unsortedArray[max];
    int* sortedArray;
    printf("\nEnter Elements for unsorted array:- \n");
    for (int index=0; index<max; index++){
        printf("\tEnter a No.:- ");
        scanf("%d", unsortedArray+index);
    }

    // Print the Unsorted Array
    printf("\nUnsorted Array:- ");
    for (int index=0; index<max; index++)
        printf(" %d", unsortedArray[index]);
    
    // Using Selection Sort Algorithm to Sort the Array
    sortedArray = insertionSort(unsortedArray, max);

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

int* insertionSort(int array[], int length){
    if (length >= 2){
        int key;
        int j;
        for (int i = 1; i <= length-1; i++){
            key = array[i];
            j = i-1;
            while(key < array[j] && j >= 0){
                array[j+1] = array[j];
                j--;
            }
            array[j+1] = key; 
        }
        return array;
    }
    else if (length == 1)
        return array;
    else 
        return NULL;
}

