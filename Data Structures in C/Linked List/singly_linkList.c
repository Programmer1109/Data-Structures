    // Singly Linked List
#include <stdio.h>
#include <stdlib.h>

struct classNode{
    int stdID;
    char name[30];
    int age;
    struct classNode *next;
};

struct classNode *start = NULL;

void createNode(struct classNode* );
void insert_begin();
void insert_end();
void insert_before_node(int );
void insert_after_node(int );
void delete_begin();
void delete_end();
void delete_before_node(int );
void delete_after_node(int );
int search_element();
int length_linkedList();
void refresh();

int main(){
    printf("Enter your choice:-\n\ta.Insert at start\n\tb.Insert at end\n\tc.Insert before node\n\td.Insert after node\n\te.Delete at start\n\t");
    printf("f.Delete at end\n\tg.Delete before node\n\th.Delete after node\n\ti.Length of linked list\n\tj.Search element\n\tk.Display\n\t");
    printf("l.Refresh\n\tm.Quit");
  while(true){
    char choice;
    scanf("%c", &choice);
    switch(choice){
      case 'a':
        insert_begin();
        break;
      case 'b':
        insert_end();
        break;
      case 'c':
        int index, value;
        printf("Enter the value at node :- ");
        scanf("%d", &value);
        index = search_element(value);
        if(index ==-1)
          printf("Error:- Entered value is not present in the linked list.\n");
        else
          insert_before_node(index);
        break;
      case 'd':
        int index, value;
        printf("Enter the value at node :- ");
        scanf("%d", &value);
        index = search_element(value);
        if(index ==-1)
            printf("Error:- Entered value is not present in the linked list.\n");
        else
            insert_after_node(index);
        break;
      case 'e':
        delete_start();
        break;
      case 'f':
        delete_end();
        break;
      case 'g':
        int index, value;
        printf("Enter the value at node :- ");
        scanf("%d", &value);
        index = search_element(value);
        if(index == -1)
            printf("Error:- Entered value is not present in the linked list.\n");
        else
            delete_before_node(index);
        break;
      case 'h':
        int index, value;
        printf("Enter the value at node :- ");
        scanf("%d", &value);
        index = search_element(value);
        if(index ==-1)
            printf("Error:- Entered value is not present in the linked list.\n");
        else
            delete_after_node(index);
        break;
      case 'i':
        int length;
        length = length_linkedList();
        printf("Length of the linked list is %d.\n", length);
        break;
      case 'j':
        int index;
        index = search_element();
        if(index ==-1)
          printf("Error:- Entered value is not present in the linked list.\n");
        else
          printf("Entered element is present at node %d.\n", index);
      case 'k':
        display_linkedList();
      case 'l':
        refresh();
      case 'm':
        refresh();
        exit(0);
        break;
      default:
        printf("Error:- Invalid Choice!!!")
    }
  }
  return 0;
}

void createNode(struct classNode* node){
    printf("\nEnter Student Details:-");
    printf("\n\tEnter Student ID:- ");
    scanf("%d", &(*node).stdID);
    printf("\tEnter Student Name:- ");
    fflush(stdin);
    gets((*node).name);
    printf("\tEnter Age of Student:- ");
    scanf("%d", &(*node).age);
    node->next = NULL;
}

void insert_begin(){
    printf("Testing Insert Begin Function:-\n");

    struct classNode *newNode;
    newNode = (struct classNode *) malloc(sizeof(struct classNode));
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

void insert_before_node(int index){
    if(index != 1){
        struct classNode* ptr;
        struct classNode* prevPtr;
        struct classNode* newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        ptr = start;
        prevPtr = NULL;
        for(int i=1; i<index; i++){
            prevPtr = ptr;
            ptr = ptr->next;
        }
        prevPtr->next = newNode;
        newNode->next = ptr;
    }
    else{
        struct classNode *newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        newNode->next = start;
        start = newNode;
    }
}

void insert_after_node(int index){
    if(index != length_linkedList()){
        struct classNode* ptr;
        struct classNode* nextPtr;

        struct classNode *newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);

        ptr = start;
        nextPtr = ptr->next;
        for(int i=1; i<index; i++){
            nextPtr = nextPtr->next;
            ptr = ptr->next;
        }
        ptr->next = newNode;
        newNode->next = nextPtr;
    }
    else{
        struct classNode* ptr = NULL;
        struct classNode *newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        for(ptr=start; ptr->next != NULL; ptr = ptr->next) ;
        ptr->next = newNode;
    }
}

void insert_end(){
    printf("Testing Insert Begin Function:-\n");

    if(start != NULL){
        struct classNode *newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
        if(newNode == NULL){
            printf("\tError: Running out of memory space\n");
            return ;
        }
        createNode(newNode);
        struct classNode *ptr;
        ptr = start;
        while(ptr->next != NULL){
            ptr = ptr->next;
        }
        printf("\t%p\t%d\t%p\n", ptr, ptr->age, ptr->next);
        ptr->next = newNode;
        printf("\t%p\t%d\t%p\n", ptr, ptr->age, ptr->next);
        printf("\t%p\t%d\t%p\n", point, point->age, point->next);
    }
    else{
        struct classNode *newNode;
        newNode = (struct classNode *) malloc(sizeof(struct classNode));
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

void delete_begin(){
    if(start != NULL){
        struct classNode* ptr;
        ptr = start;
        start = ptr->next;
        free(ptr);
    }
    else{
        printf("Error:- This list is empty. Deletion can't be performed.");
    }
}

void delete_before_node(int index){
    if(start != NULL){
        if(index > 2){
            struct classNode* prevPtr;
            struct classNode* ptr;
            prevPtr = NULL;
            ptr = start;
            for(int i=1; i<index; i++){
                prevPtr = ptr;
                ptr = ptr->next;
            }
            prevPtr->next = ptr->next;
            free(ptr);
        }
        else if(index == 2){
            struct classNode* ptr;
            ptr = start;
            start = ptr->next;
            free(ptr);
        }
        else if(index == 1)
            printf("Error:- No node is present before this node to delete.\n");
    }
    else
        printf("Error:- Linked List is Empty");
}

void delete_after_node(int index){
    if(start != NULL){
        if(index < length_linkedList()-1){
            struct classNode* ptr;
            struct classNode* nextPtr;
            ptr = start;
            nextPtr = ptr->next;
            for(int i=0; i<=index; i++){
                ptr = ptr->next;
                nextPtr = ptr->next;
            }
            ptr->next = nextPtr->next;
            free(nextPtr);
        }
        else if(index == length_linkedList()-1){
            struct classNode* ptr;
            struct classNode* prevPtr;
            ptr = start;
            while(ptr->next != NULL)
                prevPtr = ptr;
                ptr = ptr->next;
            prevPtr->next = NULL;
            free(ptr);
        }
        else if(index == length_linkedList())
            printf("Error:- No node is present after this node to delete.\n");
    }
    else
        printf("Error:- Empty Linked Lists\n\n");
}

void delete_end(){
    if(start != NULL){
        struct classNode* ptr;
        struct classNode* prevPtr;
        ptr = start;
        while(ptr->next != NULL)
            prevPtr = ptr;
            ptr = ptr->next;
        prevPtr->next = NULL;
        free(ptr);
    }
    else
        printf("Error:- This list is empty. Deletion can't be performed.");
}

int length_linkedList(){
    struct classNode *ptr;
    int length = 0;

    ptr = start;
    while(ptr != NULL){
        length++;
        ptr = ptr->next;
    }
     return length;
}

int search_element(int val){
    int index = 1;
    struct classNode *ptr;

    for(ptr = start; ptr->stdID != val; ptr=ptr->next){
        index++;
    }

    if(index == length_linkedList()+1)
        return -1;
    else
        return index;
}

void refresh(){
    struct classNode* currentPtr;
    struct classNode* nextPtr;
    int length;
    length = length_linkedList();
    currentPtr = start;
    for(int i=1; i<=length; i++){
        nextPtr = currentPtr->next;
        free(currentPtr);
        currentPtr = nextPtr;
    }
    start = NULL;
}

