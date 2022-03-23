        // Array Implementation of Stack
#include <stdio.h>
#include <stdlib.h>

int top = -1;

void push(int [], int );
void pop(int [], int );
int peek(int []);

int main(){
    printf("***************Stack Operation using Array**************\n\n\n");
    int max;
    printf("Enter no. of elements:- ");
    scanf("%d", &max);
    int stackArr[max];
    int choice;
    while(choice != 4){
     int value;
     printf("Choose your opertion:-\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4.Quit\nEnter your choice:- ");
     scanf("%d", &choice);
     switch(choice){
        case 1:
            push(stackArr, max);
            break;
        case 2:
            pop(stackArr, max);
            break;
        case 3:
            value = peek();
            printf("The value stored at top is %d\n", value);
            break;
        case 4:
            printf("Exiting...");
            break;
        default:
            printf("Error:- Invalid Input!!!\n");
      }
    }
    return 0;
}


void push(int array[], int len){
    if(top == len-1){
        printf("Error:- Overflow of elements\n");
    }
    else{
        int val;
        printf("Enter stack element value:- ");
        scanf("%d", val);
        array[++top] = val;
    }
}

void pop(int array[], int len){
    if(top == -1)
        printf("Error:- Underflow of elements\n");
    else
        top--;
}

void peek(int array[]){
    for(int i; i<=top; i++){
        if(i==top)
            return array[top];
        else
            continue;
    }
}
