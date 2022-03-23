        // Linked List Implementaton of Queues
#include <stdio.h>
#include <stdlib.h>
struct Node{
    int val;
    struct Node* next;
};

struct Node *start = NULL;

void createNode(struct Node *);
void push();
void pop();
void peek();
void refresh();

int main(){
    printf("********Queues Operation using Array**************\n\n\n");
    int choice;
    while(choice != 4){
     printf("Choose your opertion:-\n\t1.Insert element\n\t2.Delete element\n\t3.Peek top element\n\t4.Quit\nEnter your choice:- ");
     scanf("%d", &choice);
     switch(choice){
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            peek();
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
    printf("\n\tEnter Node value:- ");
    scanf("%d", &(*ptr).val);
    ptr->next = NULL;
}

void push(){
    if(start != NULL){
       struct Node* newNode;
       newNode = (struct Node *) malloc(sizeof(struct Node));
       if(newNode == NULL){
          printf("\tError: Running out of memory space\n");
          return ;
       }
       createNode(newNode);
       struct Node* ptr;
       for(ptr=start; ptr->next != NULL; ptr = ptr->next);
       ptr->next = newNode;
    }
    else{
       struct Node* newNode;
       newNode = (struct Node *) malloc(sizeof(struct Node))  ;
       if(newNode == NULL){
          printf("\tError: Running out of memory space\n");
          return ;
       }
       createNode(newNode);
       newNode->next = start;
       start = newNode;
    }
}

void pop(){
    if(start != NULL){
        struct Node* ptr;
        struct Node* prevPtr;
        ptr = start;
        start = ptr->next;
        free(ptr);
    }
    else
        printf("Error:- This list is empty. Deletion can't be performed.");
}

void peek(struct Node* ptr){
    if(start != NULL){
        struct Node* ptr;
        ptr = start;
        while(ptr->next != NULL)
            ptr = ptr->next;
        printf("Value at top = %d\n", ptr->val);
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
