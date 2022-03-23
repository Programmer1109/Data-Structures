         // Array Implementation of Queues
#include <stdio.h>
#include <stdlib.h>

int bottom = -1;
int top = -1;

void push(int [], int );
void pop(int [], int );
void peek(int []);

int main(){
    printf("********Queues Operation using Array**************\n\n\n");
    int max;
    printf("Enter no. of elements:- ");
    scanf("%d", &max);
    int queueArr[max];
    int choice;
    while(choice != 4){
     printf("Choose your opertion:-\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4.Quit\nEnter your choice:- ");
     scanf("%d", &choice);
     switch(choice){
        case 1:
            push(queueArr, max);
            break;
        case 2:
            pop(queueArr, max);
            break;
        case 3:
            peek(queueArr);
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
        if(bottom = -1)
            bottom = 0;
        int val;
        printf("Enter stack element value:- ");
        scanf("%d", val);
        array[++top] = val;
    }
}

void pop(int array[], int len){
    if(bottom == -1 || bottom > top)
        printf("Error:- Underflow of elements\n");
    else
        bottom++;
}

void peek(int array[]){
    if(top != -1){
      for(int i=bottom; i<=top; i++){
        if(i == top)
            printf("value at top = %d\n", array[top]);
        else
            continue;
      }
    }
    else
        printf("Error:- Queue is Empty\n");
}
