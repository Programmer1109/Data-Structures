         // Array Implementation of Queues
#include <stdio.h>
#include <stdlib.h>

int rear = -1;
int front = -1;
int dequeSelect;

void input_restrict_queue_main(int );
void output_restrict_queue_main(int );

void push_rear(int [], int );
void push_front(int [], int );
int pop_front(int [], int );
int pop_rear(int [], int );
int peek(int []);
void display(int [], int );

int main(){
    printf("\n\n***************\tInput-Output Restricted Queues using Array\t***************\n\n");
    int total;
    printf("Enter no. of elements:- ");
    scanf("%d", &total);
    do{
        printf("\n**********\tMAIN MENU\t**********");
        printf("\n\t1. Input Restricted Queue\n\t2. Output Restricted Queue\n\t3. Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &dequeSelect);
        switch(dequeSelect){
            case 1:
                input_restrict_queue_main(total);
                break;
            case 2:
                output_restrict_queue_main(total);
                break;
            case 3:
                front = -1;
                rear = -1;
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(dequeSelect != 3);
    return 0;
}

void input_restrict_queue_main(int max){
    printf("\n\n***************\tInput Restricted Queues using Array\t***************\n");
    int item, choice;
    int inputRestrictedqueue[max];
    do{
        printf("\n**********\tMAIN MENU\t**********");
        printf("\n\t1. Insert Element\n\t2. Delete Element at Front\n\t3. Delete Element at Rear\n\t4. Peek top element\n\t5. Display Queue\n\t6. Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                push_rear(inputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                break;
            case 2:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                item = pop_front(inputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d\tElement = %d", front, rear, item);
                break;
            case 3:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                item = pop_rear(inputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d\tElement = %d", front, rear, item);
                break;
            case 4:
                item = peek(inputRestrictedqueue);
                if(item == -1)
                    printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
                else
                    printf("\nResult:- Data[%d] = %d", front, item);
                break;
            case 5:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);                
                display(inputRestrictedqueue, max);
                break;
            case 6:
                front = -1;
                rear = -1;
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(choice != 6);
}

void output_restrict_queue_main(int max){
    printf("\n\n********\tOutput Restricted Queues using Array\t**************\n");
    int item, choice;
    int outputRestrictedqueue[max];
    do{
        printf("\n**********\tMAIN MENU\t**********");
        printf("\n\t1. Insert Element at Rear end\n\t2. Insert Element at Front end\n\t3. Delete Element\n\t4. Peek top element\n\t5. Display Queue\n\t6. Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                push_rear(outputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                break;
            case 2:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                push_front(outputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                break;
            case 3:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);
                item = pop_front(outputRestrictedqueue, max);
                printf("\nResults:- Front = %d\tRear = %d\tElement = %d", front, rear, item);
                break;
            case 4:
                item = peek(outputRestrictedqueue);
                if(item == -1)
                    printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
                else
                    printf("\nResult:- Data[%d] = %d", front, item);
                break;
            case 5:
                printf("\nResults:- Front = %d\tRear = %d", front, rear);                
                display(outputRestrictedqueue, max);
                break;
            case 6:
                front = -1;
                rear = -1;
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(choice != 6);
}

void push_rear(int array[], int len){
    if ((rear == len-1 && front == 0) || rear == front-1){
        printf("\nError:- Overflow of elements\n");
    }
    else if (front == -1 && rear == -1){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        front = 0;
        rear = 0;
        array[rear] = val;
    }
    else if (rear == len-1 && front != 0){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        rear = 0;
        array[rear] = val;
    }
    else{
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[++rear] = val;
    }
}

//Only for Output Deque
void push_front(int array[], int len){
    if((rear == len-1 && front == 0) || rear == front-1){
        printf("\nError:- Overflow of elements\n");
    }
    else if(front == -1 && rear == -1){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        front = 0;
        rear = 0;
        array[front] = val;
        printf("\nQueue[%d] = %d", front, array[front]);
    }
    else if(rear != len-1 && front == 0){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        front = len-1;
        array[front] = val;
        printf("\nQueue[%d] = %d", front, array[front]);
    }
    else{
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        printf("\nQueue[%d] =", front);
        array[--front] = val;
        printf(" %d", array[front]);
    }
}

int pop_front(int array[], int len){
    if(front == -1 && rear == -1){
        printf("\nError:- Underflow of elements");
        return -1;
    }
    else if(front == rear){
        int value = array[front];
        array[front] = -1;
        front = -1;
        rear =-1;
        return value;
    }
    else if(front == len-1 && rear < front){
        int value = array[front];
        array[front] = -1;
        front = 0;
        return value;
    }
    else{
        int value = array[front];
        array[front++] = -1;
        return value;
    }
}

//Only for Input deque
int pop_rear(int array[], int len){
    if(front == -1 && rear == -1){
        printf("\nError:- Underflow of elements");
        return -1;
    }
    else if(front == rear){
        int value = array[rear];
        array[rear] = -1;
        front = -1;
        rear =-1;
        return value;
    }
    else if (rear == 0 && front !=0){
        int value = array[rear];
        array[rear] = -1;
        rear = len-1;
        return value;
    }
    else{
        int value;
        value = array[rear];
        array[rear--] = -1;
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
    else if(front <= rear){
        printf("\nDisplaying the Queue...");
        for(int index = front; index<=rear; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    }
    else if(front >= rear){
        printf("\nDisplaying the Queue...");
        for(int index = front; index <= len-1; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
        for(int index = 0; index <= rear; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    }
}
