        // Linked List Implementation of Stacks
#include <stdio.h>
#include <stdlib.h>

struct Node{
    int node_val;
    struct Node* next;
};
struct Node* start = NULL;

void createNode(struct Node* );
void push();
void pop();
int peek();
void referesh();

int main(){
    printf("********Stack Operation using Linked List**************\n\n\n");
    int max;
    printf("Enter no. of elements:- ");
    scanf("%d", &max);
    int choice;
    while(choice != 4){
     int value;
     printf("Choose your operation:-\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4.Quit\nEnter your choice:- ");
     scanf("%d", &choice);
     switch(choice){
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            value = peek();
            printf("The value stored at top is %d\n", value);
            break;
        case 4:
            refresh();
            printf("Exiting...");
            break;
        default:
            printf("Error:- Invalid Input!!!\n");
      }
    }
    return 0;
}

void createNode(struct Node* ptr){
    printf("Enter Node value:- ");
    scanf("%d", &ptr->node_val);
    ptr->next = NULL;
}

void push(){
    if(start != NULL){
        struct classNode *newNode;
        newNode = (struct Node *) malloc(sizeof(struct Node));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        struct Node *ptr;
        ptr = start;
        while(ptr->next != NULL)
            ptr = ptr->next;

        printf("\t%p\t%d\t%p\n", ptr, ptr->age, ptr->next);
        ptr->next = newNode;
        printf("\t%p\t%d\t%p\n", ptr, ptr->age, ptr->next);
        printf("\t%p\t%d\t%p\n", point, point->age, point->next);
    }
    else{
        struct Node *newNode;
        newNode = (struct Node *) malloc(sizeof(struct Node));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        newNode->next = start;
        printf("\t%p\t%d\t%p\n", start, start->age, start->next);
        start = newNode;
        printf("\t%p\t%d\t%p\n", start, start->age, start->next);
        printf("\t%p\t%d\t%p\n", newNode, newNode->age, newNode->next);
    }
}

void pop(){
    if(start != NULL){
        struct Node* ptr;
        struct Node* prevPtr;
        ptr = start;
        while(ptr->next != NULL){
            prevPtr = ptr;
            ptr = ptr->next;
        }
        prevPtr->next = NULL;
        free(ptr);
    }
    else
        printf("Error:- This stack is empty. Hence, Deletion can't be performed.");
}

void peek(){
    if(start != NULL){
        struct Node* ptr;
        ptr = start;
        while(ptr->next != NULL)
            ptr = ptr->next;
        return ptr->node_val;
    }
    else
        printf("Error:- List is Empty!!!");
}

void refresh(){
    if(start != NULL){
      struct Node* ptr;
      struct Node* nextPtr;
      int length;
      ptr = start;
      nextPtr = ptr->next;
      length = getLength();
      for(int i=0; i<length; i++){
         nextPtr = ptr->next;
         free(ptr);
         ptr = nextPtr;
      }
      start = NULL;
    }
}
