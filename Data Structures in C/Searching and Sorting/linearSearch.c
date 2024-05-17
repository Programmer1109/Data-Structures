#include <stdio.h>
#include <conio.h>

int linearSearch(int [], int );

int main(){
    printf("\n*************** \tLINEAR SEARCH using Array\t ***************\n\n");
    int max, index;
    
    printf("\nEnter No. of elements: ");
    scanf("%d", &max);
    int searchArray[max];
    printf("Enter sorted list:-");
    for(int i = 0; i<max; i++){
        printf("\nEnter value of element:- ");
        scanf("%d", searchArray+i);
    }
    
    index = linearSearch(searchArray, max);
    if(index != -1)
        printf("\nResult:- Entered element found in the Array at index %d.", index+1);
    else
        printf("\nResult:- Entered element not found in the Array.");
    
    getch();
    return 0;
}

int linearSearch(int array[], int max){
    int key;
    printf("\nEnter value to be searched:- ");
    scanf("%d", &key);
    for(int i=0; i <= max-1; i++){
        if(array[i] == key)
            return i;
        else
            continue;
    }
    return -1;
}
