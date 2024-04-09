// Implementation of Circular Linked List in C Programming Language
#include<stdio.h>
#include<stdlib.h>

#define operations 13

struct node{
    int rollNo;
    struct node* next;
};

struct node* start = NULL;

//Functions to implement a linked list
        //Insertion Operations
struct node* insert_at_begin(struct node* );
struct node* insert_at_end(struct node* );
struct node* insert_before_node(struct node* );
struct node* insert_after_node(struct node* );
        //Deletion Operations
struct node* delete_begin(struct node* );
struct node* delete_end(struct node* );
struct node* delete_before_node(struct node* );
struct node* delete_after_node(struct node* );
struct node* destroy_list(struct node*);
        //Traversing List
void display_list(struct node* );
int searching(struct node* , int );
int length_of_list(struct node* );

int main(){
    printf("\t\t\t\tIMPLEMENTATION of CIRCULAR LINKED LIST in C \n");
    int option;
    do{
    int index, num, length;
    printf("\n********** MAIN MENU **********");
    printf("\n\t1. Insert node at begining");
    printf("\n\t2. Insert node at end");
    printf("\n\t3. Insert node before given node");
    printf("\n\t4. Insert node after given node");
    printf("\n\t5. Delete node at Begining");
    printf("\n\t6. Delete node at End");
    printf("\n\t7. Delete node before given Node");
    printf("\n\t8. Delete node after given Node");
    printf("\n\t9. Search Node in the Linked List");
    printf("\n\t10. Display Linked List");
    printf("\n\t11. Destroy Linked List");
    printf("\n\t12. Length of Linked List");
    printf("\n\t13. Exit Program");
    printf("\nEnter your choice:- ");
    scanf("%d", &option);
    if(option < operations){
        switch(option){
            case 1:
                start = insert_at_begin(start);
                break;
            case 2:
                start = insert_at_end(start);
                break;
            case 3:
                start = insert_before_node(start);
                break;
            case 4:
                start = insert_after_node(start);
                break;
            case 5:
                start = delete_begin(start);
                break;
            case 6:
                start = delete_end(start);
                break; 
            case 7:
                start = delete_before_node(start);
                break;
            case 8:
                start = delete_after_node(start);
                break;
            case 9:
                printf("Enter Roll No. to be searched:- ");
                scanf("%d", &num);
                index = searching(start, num);
                if(index == -1)
                    printf("\nSearch Result:- Entered Node is not present in the Linked List\n");
                else
                    printf("\nSearch Result:- Entered Node is present in the Linked List at index %d\n", index);
                break;
            case 10:
                display_list(start);
                break;
            case 11:
                start = destroy_list(start);
                break;
            case 12:
                length = length_of_list(start);
                printf("\nLength of List = %d\n", length);
                break;
        }
    }
    else if(option == operations){
        start = destroy_list(start);
        printf("\n*********** END OF PROGRAM ***********");
    }
    else
        printf("\nError:- Invalid operation!!!");
    }while(option != operations);
    return 0;
}

struct node* insert_at_begin(struct node* head){
    printf("\nInserting Node at the Start of List...");
    struct node* newNode;
    int data; 
    printf("\nEnter data for node:- ");
    scanf("%d", &data);
    newNode = (struct node*) malloc(sizeof(struct node));
    if (newNode == NULL)
        printf("\nError:- coludn't allocate space for the node!!!");
    else if(head == NULL){
        printf("\nSuccess:- Memory Allocated Successfully...");
        newNode->rollNo = data;
        newNode->next = newNode;
        head = newNode;
        printf("\nStart = %x\tNewNode:- Roll No. = %d\tNext Node = %x", start, head->rollNo, head->next);
    }
    else{
        printf("\nSuccess:- Memory Allocated Successfully..."); 
        newNode->rollNo = data;
        struct node* last;
        last = head;
        while(last->next != head)
            last = last->next;
        printf("\nBefore:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
        newNode->next = head;
        head = newNode;
        last->next = newNode;
        printf("\nAfter:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, newNode->rollNo, newNode->next);
        printf("\nNewNode:- Roll No. = %d\tNext Node = %x", newNode->rollNo, newNode->next);
    }
    return head;
}

struct node* insert_before_node(struct node* head){
    printf("\nInserting Node Before given Node...");
    if(head != NULL){
        struct node* newNode;
        struct node* prevPtr;
        int data, val;
        printf("\nEnter the Roll No. before which node is to be inserted:- ");
        scanf("%d", &val);
        printf("\nEnter data for the node:- ");
        scanf("%d", &data);
        newNode = (struct node*) malloc(sizeof(struct node));
        if(newNode != NULL){
            printf("\nSuccess:- Memory Allocated Successfully...");    
            if(searching(head, val) != -1){
                if(head->rollNo == val){
                    newNode->rollNo = data;
                    struct node* last;
                    last = head;
                    while(last->next != head)
                        last = last->next;
                    newNode->next = head;
                    head = newNode;
                    last->next = newNode;
                }
                else{
                    newNode->rollNo = data;
                    struct node *ptr;
                    ptr = start;
                    while(ptr->rollNo != val){
                        printf("\nTraversing through the List...");
                        prevPtr = ptr;
                        ptr = ptr->next;
                    }
                    prevPtr->next = newNode;
                    newNode->next = ptr;
                }
            }
            else
                printf("\nError:- Entered Node is not present in Linked List...");
        }
        else
            printf("\nError:- Couldn't allocate space for node...");
    }
    else
        printf("\nError:- EMPTY LIST!!! Can't perform opertaton...");
    return head;
}

struct node* insert_after_node(struct node* head){
    printf("\nInserting Node After given Node...");
    if(head != NULL){
        int val;
        printf("\nEnter the Roll No. after which node is to be inserted:- ");
        scanf("%d", &val);
        if(searching(head, val) != -1){
            struct node* newNode;
            newNode = (struct node*) malloc(sizeof(struct node));
            if(newNode != NULL){
                struct node *ptr, *nextPtr;
                int data;
                printf("\nEnter data for the node:- ");
                scanf("%d", &data);
                struct node* last;
                last = head;
                while(last->next != head)
                    last = last->next;
                if(last->rollNo == val){
                    printf("\nSuccess:- Memory Allocated Successfully...\n");
                    newNode->rollNo = data;
                    last->next = newNode;
                    newNode->next = start;
                }
                else{
                    printf("\nSuccess:- Memory Allocated Successfully...\n");
                    newNode->rollNo = data;
                    ptr = start;
                    nextPtr = start->next;
                    while(ptr->rollNo != val){
                        //printf("Traversing through the List...\n");
                        ptr = ptr->next;
                        nextPtr = ptr->next;
                    }
                    ptr->next = newNode;
                    newNode->next = nextPtr;
                }
            }
            else
                printf("\nError:- Couldn't allocate space for node...");
        }
        else
            printf("\nError:- Couldn't allocate space for node...");
    }
    else
        printf("\nError:- EMPTY LIST!!! Can't perform opertaton...");
    return head;
}

struct node* insert_at_end(struct node* head){
    printf("\nInserting Node at the End...");
    struct node *last, *newNode;
    int data;
    
    if(head == NULL)
        head = insert_at_begin(head);
    else{
        printf("\nSuccess:- Memory Allocated Successfully...");    
        printf("\nEnter the data : ");
        scanf("%d", &data);
        newNode = (struct node *)malloc(sizeof(struct node));
        if(newNode == NULL)
            printf("\nError:- Couldn't Allocate Memory");
        else{
            newNode->rollNo = data;
            newNode->next = NULL;
            last = start;
            while(last->next != head)
                last = last->next;
            printf("\nBefore:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
            last->next = newNode;
            newNode->next = head;
            printf("\nAfter:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
            printf("\nNewNode:- Roll No. = %d\tNext Node = %x", newNode->rollNo, newNode->next);
        }
    }
    return head;
}


struct node* delete_begin(struct node* head){
    printf("\nDeleting the first Node...\n"); 
    if(head != NULL){
        if(head->next != head){
            struct node* temp;
            struct node* last = head;
            while(last->next != head)
                last = last->next;
            printf("\nBefore:- Start = %d %x\n\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
            last->next = head->next;
            temp = head;
            head = head->next;
            printf("\nAfter:- Start = %d %x\n\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
            printf("\nDeleted Node:- Data = %d   Address = %x", temp->rollNo, temp->next);
            free(temp);
        }
        else{
            printf("Note:- Only one element in the List");
            printf("\nBefore:- Start = %d %x", head->rollNo, head->next);
            free(head);
            printf("\nAfter:- Start = %d %x", head->rollNo, head->next);
            head = NULL;
            //printf("\nAfter:- Start = %d %x", head->rollNo, head->next);
        }
    }
    else
        printf("\nError:- Can't delete from an EMPTY Linked List...");
    return head;
}

struct node* delete_before_node(struct node* head){
    printf("\nDeleting Node Before given Node...");
    struct node* ptr;
    struct node* nextPtr;
    struct node* prevPtr;
    int data;
    if(start != NULL){
        printf("\nEnter the Roll No. of the node before which deletion is to take place: ");
        scanf("%d", &data);
        if(searching(head, data) != -1){
            if(head->rollNo == data)
                printf("\nError:- No Node before this node. Deletion can't be performed...");
            else if(head->next->rollNo == data){
                struct node* last;
                struct node* temp;
                last = head;
                while(last->next != head)
                    last = last->next;
                last->next = head->next;
                temp = head;
                head = head->next;
                free(temp);
            }
            else{
                ptr = start;
                nextPtr = start->next;
                while(nextPtr->rollNo != data){
                    prevPtr = ptr;
                    ptr = ptr->next;
                    nextPtr = ptr->next;
                }
                printf("\nPrevPtr-> %d %x\nPtr-> %d %x\nNextPtr-> %d %x", prevPtr->rollNo, prevPtr->next, ptr->rollNo, ptr->next, nextPtr->rollNo, nextPtr->next);
                prevPtr->next = nextPtr;
                free(ptr);
            }
        }
        else
            printf("\nError:- Entered element is not present in the linked list...");
    }
    else
        printf("\nError:- EMPTY Linked List...\n");
    return head;
}

struct node* delete_after_node(struct node* head){
    printf("\nDeleting Node After given Node...\n");
    struct node* ptr;
    struct node* last;
    struct node* nextPtr;
    int data;
    if(start != NULL){
        printf("\nEnter the Roll No. of the node after which deletion is to take place: ");
        scanf("%d", &data);
        if(searching(start, data) != -1){
            last = start;
            while(last->next != head)
                last = last->next;
            if(last->rollNo == data)
                printf("\nError:-  No Node after this node. Deletion can't be performed...");
            else{   
                ptr = start;
                nextPtr = start->next;
                while(ptr->rollNo != data){
                    ptr = ptr->next;
                    nextPtr = ptr->next;
                }
                printf("\nPtr-> %d %x\nNextPtr-> %d %x\n", ptr->rollNo, ptr->next, nextPtr->rollNo, nextPtr->next);
                ptr->next = nextPtr->next;
                printf("\nPtr-> %d %x\nNextPtr-> %d %x\n", ptr->rollNo, ptr->next, nextPtr->rollNo, nextPtr->next);
                free(nextPtr);
            }
        }
        else
            printf("\nError:- Entered value is not present the List!!!");
    }
    else
        printf("\nError:- EMPTY Linked List...");
    return head;
}

struct node* delete_end(struct node* head){
    printf("\nDeleting the last Node...");
    if(head != NULL){
        if(head->next == head){
            printf("Note:- Only one element in the List");
            printf("\nBefore:- Start = %d %x", head->rollNo, head->next);
            free(head);
            printf("\nAfter:- Start = %d %x", head->rollNo, head->next);
            head = NULL;
            //printf("\nAfter:- Start = %d %x", head->rollNo, head->next);
        }
        else{
            struct node* last;
            struct node* prev;
            last = start;
            while(last->next != head){
                prev = last;
                last = last->next;
            }
            printf("\nBefore:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, last->rollNo, last->next);
            prev->next = head;
            printf("\nAfter:- Start = %d %x\tLast = %d %x", head->rollNo, head->next, prev->rollNo, prev->next);
            printf("\nDeleted Node:- Data = %d   Address = %x", last->rollNo, last->next);
            free(last); 
        }
    }
    else
        printf("\nError:- EMPTY Linked List!!!");
    return head;
}

struct node* destroy_list(struct node* head){
    printf("\nDestroying the entire list...");
    if(head != NULL){
        struct node* last;
        last = head;
        while(last->next != head)
            last = last->next;
        while(start->next != head){
            printf("\nCurrent Last Node-> Roll No.:- %d\tAddress:- %x", last->rollNo, last->next);
            head = delete_end(head);
        }
        printf("\nOutside Loop...");
        printf("\nCurrent Last Node-> Roll No.:- %d\tAddress:- %x", last->rollNo, last->next);
        free(head);
        head = NULL;
        printf("\nNew Last Node-> Roll No.:- %d\tAddress:- %x", last->rollNo, last->next);
    }
    else
        printf("Error:- the list is already EMPTY...");
    return head;
}

void display_list(struct node* head){
    printf("\nDisplaying the Linked List...\n");
    struct node* ptr = head;
    if(head == NULL)
        printf("Error:- EMPTY LIST...\n");
    else{
        while(ptr->next != head){
            printf("Current Node:- Data = %d & Address = %x\tNext Node = %x\n", ptr->rollNo, ptr, ptr->next);
            ptr = ptr->next;
        }
        printf("Current Node:- Data = %d & Address = %x\tNext Node = %x\n", ptr->rollNo, ptr, ptr->next);
    } 
}

int searching(struct node* head, int key){
    printf("\nSearching for Node in the Singly Linked List...");
    //printf("\nkey= %d", key);
    if(head != NULL){
        //printf("\ninside if...");
        struct node* ptr;
        ptr = head;
        //printf("\nPtr-> %d %x", ptr->rollNo, ptr->next, ptr);
        int test;
        for(int i=0; ptr->next != head; i++){
            //printf("\nIteration = %d\tPtr-> %d %x", i, ptr->rollNo, ptr->next, ptr);
            if(ptr->rollNo == key){
                //printf("inside if-> key = %d", key);
                return i+1;
            }
            ptr = ptr->next;
        }
        //printf("\nOut of for...");
        if(ptr->rollNo == key)
            return length_of_list(head); 
        else
            return -1;
    }
    else{
        printf("\nError:- EMPTY List...");
        return -1;
    }
}

int length_of_list(struct node* head){
    printf("\nCouting nodes of the Linked List...");
    if(head == NULL)
        return 0;
    else{
        struct node* ptr;
        int len;
        ptr = start;
        ptr = ptr->next;
        for(len=1; ptr != start; len++){
            ptr = ptr->next;
        }
        return len;
    }
}
