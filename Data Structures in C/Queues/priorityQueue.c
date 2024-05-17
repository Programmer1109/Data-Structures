        // Linked List Implementation of Queue
#include <stdio.h>
#include <stdlib.h>

struct node{
    int rollNo;
    int priority;
    struct node* next;
};

struct node* insert(struct node* );
struct node* delete(struct node* );
int peek(struct node* );
struct node* destroy_queue(struct node* );
void display(struct node* );
int queue_length(struct node* );

struct node* start = NULL;

int main(){
    printf("\n**************\tIMPLEMENTATION of Priority Queue using Linked List\t**************\n\n");
    int choice, length, value;
    do{
     int value;
     printf("\n\n***************\tMAIN MENU\t***************");
     printf("\n\t1. Insert element\n\t2. Delete element\n\t3. Peek top element\n\t4. Destroy Queue\n\t5. Display Queue\n\t6. Queue Length\n\t7. Quit");
     printf("\nEnter your choice:- ");
     scanf("%d", &choice);
     switch(choice){
        case 1:
            start = insert(start);
            break;
        case 2:
            start = delete(start);
            break;
        case 3:
            value = peek(start);
            if(value != -1)
                printf("\nValue @ front = %d", value);
            else
                printf("\nNo value at front!!!");
            break;
        case 4:
            start = destroy_queue(start);
            break;
        case 5:
            display(start);
            break;
        case 6:
            length = queue_length(start);
            printf("\nNo. of elements in the QUEUE = %d", length);
            break;
        case 7:
            start = destroy_queue(start);
            break;
        default:
            printf("Error:- Invalid Input!!!\n");
      }
    }while(choice != 7);
    printf("\n\n**********\tEND of PROGRAM\t**********\n\n");
    return 0;
}

struct node* insert(struct node* head){
    printf("\nInserting Node at the End...");
    struct node *newNode;
    int data, predominance;
    printf("\nEnter Data to be pushed on queue:- ");
    scanf("%d", &data);
    printf("Enter Priority of the node:- ");
    scanf("%d", &predominance);
    newNode = (struct node*) malloc(sizeof(struct node));
    if(newNode == NULL)
        printf("\nError:- Couldn't Allocate Memory!!!");
    else{
        printf("\nSuccess:- Memory Allocated Successfully...");
        newNode->rollNo = data;
        newNode->priority = predominance;
        newNode->next = NULL;
        if (head == NULL)
            head = newNode;
        else if(newNode->priority < head->priority){
            newNode->next = head;
            head = newNode;
            printf("\nStart Node:- Roll No. = %d\tPriority = %d\tNext Node = %x", head->rollNo, head->priority, head->next);
            printf("\nNewNode:- Roll No. = %d\tNext Node = %x", newNode->rollNo, newNode->next);
        }
        else{
            struct node* ptr;
            struct node* prevPtr;
            ptr = head;
            prevPtr = NULL;
            while (ptr->next != NULL && newNode->priority >= ptr->priority){
                prevPtr = ptr;
                ptr = ptr->next;
            }
            newNode->next = ptr;
            prevPtr->next = newNode;
            printf("\nPre-Pointer:- Roll No. = %d\tPriority = %d\tNext Node = %x", prevPtr->rollNo, prevPtr->priority, prevPtr->next);
            printf("\nNewNode:- Roll No. = %d\tNext Node = %x", newNode->rollNo, newNode->next);
            printf("\nPointer:- Roll No. = %d\tPriority = %d\tNext Node = %x", ptr->rollNo, ptr->priority, ptr->next);
        }
        printf("\nNewNode:- Roll No. = %d\tNext Node = %x", newNode->rollNo, newNode->next);
    }
    return head;
}

struct node* delete(struct node* head){
    printf("\nDeleting the first Node...\n");
    struct node* temp = head;
    if(head != NULL){
        temp = head;
        head = head->next;
        printf("\nDeleted Node:- Data = %d   Address = %x", temp->rollNo, temp->next);
        free(temp);
    }
    else
        printf("\nError:- Can't delete from an EMPTY Linked List");
    return head;
}

int peek(struct node* head){
    if(head != NULL)
        return head->rollNo;
    else{
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
        return -1;
    }
}

void display(struct node* head){
    if(head != NULL){
        struct node* ptr;
        ptr = head;
        for(int iter = 1; ptr != NULL; iter++){
            printf("\nData[%d] = %d\tAddress = %x\tNext Node = %x", ptr->priority, ptr->rollNo, ptr, ptr->next);
            ptr = ptr->next;
        }
        printf("\n");
    }
    else
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
}

struct node* destroy_queue(struct node* head){
    if(head != NULL){
        //printf("\nLast Node:- Roll No. = %d\tAddress = %x\tNext Node = %x", head->rollNo, head, head->next);
        while(head != NULL){
            printf("\nStart Node:- Data = %d\tPriority = %d\tAddress = %x\tNext = %x", head->rollNo, head->priority, head, head->next);
            head = delete(head);
        }
        head = NULL;
    }
    else
        printf("\nUNDERFLOW ERROR:- EMPTY QUEUE!!!");
    return head;
}

int queue_length(struct node* head){
    if(head != NULL){
        struct node* ptr;
        int count = 0;
        ptr = head;
        for(count = 0; ptr != NULL; count++)
            ptr = ptr->next;
        return count;
    }
    else
        return 0;
}
