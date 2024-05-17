#include<stdio.h>

int binarySearch(int [], int );

int main(){
    printf("\n*************** \tBINARY SEARCH using Array\t ***************\n\n");
    int max, index;
    char choice='y';
    while(choice != 'n'){
        printf("\nEnter No. of elements: ");
        scanf("%d", &max);
        int searchArray[max];
        printf("Enter sorted list:-");
        for(int i = 0; i<max; i++){
            printf("\nEnter value of element:- ");
            scanf("%d", searchArray+i);
        }
        index = binarySearch(searchArray, max);
        if(index != -1)
            printf("\nResult:- Entered element found in the Array at index %d.", index+1);
        else
            printf("\nResult:- Entered element not found in the Array.");
        fflush(stdin);
        printf("\nEnter (Y/N):- ");
        scanf("%c", &choice);
        printf("\n%c\n", choice);
    }
    return 0;
}

int binarySearch(int array[], int max){
    int first=0, last=max-1, mid;
    int key;
    printf("\nEnter value to be searched:- ");
    scanf("%d", &key);
    for(int i=0; first<=last; i++){
        mid = (first+last)/2;
        if(array[mid] == key)
            return mid;
        else if(array[mid] < key)
            first = mid + 1;
        else if(array[mid] > key)
            last = mid - 1;
    }
    return -1;
}
