#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int rear = -1;
int front =-1;

void push(int [], int);
int pop(int [], int );
int peek(int []);
void display(int [], int );

int main(){
    printf("***************\t\tCircular Queues Operation using Array\t\t***************\n\n");
    int max, choice, element;
    printf("Enter no. of elements:- ");
    scanf("%d", &max);
    int cQueueArr[max];
    do{
        printf("\n\n**********\tMAIN MENU\t**********");
        printf("\n\t1. Insert Element\n\t2. Delete Element\n\t3. Peek Top Element\n\t4. Display Queue\n\t5.Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                push(cQueueArr, max);
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                break;
            case 2:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                element = pop(cQueueArr, max);
                printf("\nResults:- Front = %d\tRear = %d\tElement = %d", front, rear, element);
                break;
            case 3:
                element = peek(cQueueArr);
                if(element == -1)
                    printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
                else
                    printf("\nResult:- Data[%d] = %d", front, element);
                break;
            case 4:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);                
                display(cQueueArr, max);
                break;
            case 5:
                //Nothing Here
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(choice != 5);
    return 0;
}

void push(int array[], int len){
    if((rear == len-1 && front == 0) || (rear == front - 1)){
        printf("\nError:- Overflow of elements!!!");
    }
    else if(front == -1 && rear == -1){
        front = 0;
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[++rear] = val;
    }
    else if(front != 0 && rear == len-1){
        rear = 0;
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[rear] = val;
    }
    else{
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[++rear] = val;
    }
}

int pop(int array[], int len){
    int value;
    if(front == -1 && rear == -1){
        printf("\nError:- Underflow of elements");
        return -1;
    }
    else if((front != -1 && rear != -1) && front == rear){
        value = array[front];
        array[front] = -1;
        front = -1;
        rear = -1;
        return value;
    }
    else if(front == len-1 && rear < front){
        value = array[front];
        array[front] = -1;
        front = 0;
        return value;
    }
    else{
        value = array[front];
        array[front++] = -1;
        return value;
    }
}

int peek(int array[]){
    if(front != -1)
        return array[front];
    else
        return -1;        
}

void display(int array[], int len){
    if(front == -1 && rear == -1)
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
    else if(front < rear){
        printf("\nDisplaying the Queue...");
        for(int index = front; index<=rear; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    }
    else if(front > rear){
        printf("\nDisplaying the Queue...");
        for(int index = front; index <= len-1; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
        for(int index = 0; index <= rear; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    }
}
