         // Array Implementation of Queues
#include <stdio.h>
#include <stdlib.h>

#define max 20

int rearA = -1;
int frontA = -1;
int rearB = -1;
int frontB = -1;
int QueueArray[max];


void queueA_operations();
void queueB_operations();

void queueA_push(int [], int );
void queueB_push(int [], int );
int queueA_pop(int [], int );
int queueB_pop(int [], int );
int queueA_peek(int []);
int queueB_peek(int []);
void display(int []);

int main(){
    printf("\n\n***************\tMultiple Queues using Array\t***************\n\n");
    int queueSelect;
    do{
        printf("\n**********\tMAIN MENU\t**********");
        printf("\n\t1. Operations on Queue A\n\t2. Operations on Queue B\n\t3. Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &queueSelect);
        switch(queueSelect){
            case 1:
                queueA_operations();
                break;
            case 2:
                queueB_operations();
                break;
            case 3:
                frontA = -1;
                rearA = -1;
                frontB = -1;
                rearB = -1;
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(queueSelect != 3);
    return 0;
}

void queueA_operations(){
    int choice, value;
    do{
        printf("\n\n**********\t\tMAIN MENU\t**********");
        printf("\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4. Display Queue\n\t5.Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nResults:- FrontA = %d\tRearA = %d", frontA, rearA);
                queueA_push(QueueArray, max);
                printf("\nResults:- FrontA = %d\tRearA = %d", frontA, rearA);
                break;
            case 2:
                printf("\nResults:- FrontA = %d\tRearA = %d", frontA, rearA);
                value = queueA_pop(QueueArray, max);
                printf("\nResults:- FrontA = %d\tRearA = %d\t Element = %d", frontA, rearA, value);
                break;
            case 3:
                value = queueA_peek(QueueArray);
                if(value == -1)
                    printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
                else
                    printf("\nResult:- Data[%d] = %d", frontA, value);
                break;
            case 4:
                printf("\nResults:- FrontA = %d\tRearA = %d", frontA, rearA);                
                display(QueueArray);
                break;
            case 5:
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(choice != 5);
}

void queueB_operations(){
    int choice, value;
    do{
        printf("\n\n**********\t\tMAIN MENU\t**********");
        printf("\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4. Display Queue\n\t5.Quit");
        printf("\nEnter your choice:- ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nResults:- FrontB = %d\tRearB = %d", frontB, rearB);
                queueB_push(QueueArray, max);
                printf("\nResults:- FrontB = %d\tRearB = %d", frontB, rearB);
                break;
            case 2:
                printf("\nResults:- FrontB = %d\tRearB = %d", frontB, rearB);
                value = queueB_pop(QueueArray, max);
                printf("\nResults:- FrontB = %d\tRearB = %d\tElement = %d", frontB, rearB, value);
                break;
            case 3:
                value = queueB_peek(QueueArray);
                if(value == -1)
                    printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
                else
                    printf("\nResult:- Data[%d] = %d", frontB, value);
                break;
            case 4:
                printf("\nResults:- FrontB = %d\tRearB = %d", frontB, rearB);                
                display(QueueArray);
                break;
            case 5:
                break;
            default:
                printf("Error:- Invalid Input!!!\n");
        }
    }while(choice != 5);
}

void queueA_push(int array[], int len){
    if(rearA == rearB-1){
        printf("\nError:- Overflow of elements\n");
    }
    else if(frontA == -1 && rearA == -1){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        frontA = 0;
        rearA = 0;
        array[rearA] = val;
    }
    else{
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[++rearA] = val;
    }
}

void queueB_push(int array[], int len){
    if(rearB == rearA+1){
        printf("\nError:- Overflow of elements\n");
    }
    else if(frontB == -1 && rearB == -1){
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        frontB = len-1;
        rearB = len-1;
        array[rearB] = val;
    }
    else{
        int val;
        printf("\nEnter queue element value:- ");
        scanf("%d", &val);
        array[--rearB] = val;
    }
}

int queueA_pop(int array[], int len){
    if(frontA == -1 && rearA == -1){
        printf("\nError:- Underflow of elements");
        return -1;
    }
    else if(frontA == rearA){
        int value = array[frontA];
        array[frontA] = -1;
        frontA = -1;
        rearA = -1;
        return value;
    }
    else{
        int value = array[frontA];
        array[frontA++] = -1;
        return value;
    }
}

int queueB_pop(int array[], int len){
    if(frontB == -1 && rearB == -1){
        printf("\nError:- Underflow of elements");
        return -1;
    }
    else if(frontB == rearB){
        int value = array[frontB];
        array[frontB] = -1;
        frontB = -1;
        rearB = -1;
        return value;
    }
    else{
       int value = array[frontB]; 
       array[frontB--] = -1;
       return value;
    }
}

int queueA_peek(int array[]){
    if(frontA != -1)
        return array[frontA];
    else
        return -1;        
}

int queueB_peek(int array[]){
    if(frontB != -1)
        return array[frontB];
    else
        return -1;        
}

void display(int array[]){
    // Check if QUEUE A is EMPTY; if not display QUEUE A
    if (frontA == -1 && rearA == -1)
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE A!!!");
    else if (frontA != -1 && rearA != -1)
        printf("\nDisplaying Queue A...");
        for(int index = frontA; index <= rearA; index++)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    // Check if QUEUE B is EMPTY; if not display QUEUE B
    if (frontB == -1 && rearB == -1)
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE B!!!");
    else if (frontB != -1 && rearB != -1){
        printf("\nDisplaying Queue B...");
        for(int index = frontB; index >= rearB; index--)
            printf("\nQUEUE[%d] = %d", index, array[index]);
    }
}

