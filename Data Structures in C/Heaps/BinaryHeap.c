#include <stdio.h>
#include <conio.h>

#define MAX 50

int heapSize = 1;

void min_heap_operations();
void max_heap_operations();

void insert_heap(int [], char* );
int delete_heap(int [], char* );
int search_heap(int [], int );
void decrease_key(int [], int , int );
void increase_key(int [], int , int );
int get_maximum(int []);
int get_minimum(int []);
void Heapify(int [], char* );

int main(){
    int choice;
    printf("***************\tIMPLEMENTATION OF BINARY HEAP IN C\t***************\n\n");
    printf("Choose your operation:-\n\t1. Min Binary Heap Operations\n\t2. Max Binary Heap Operations\n\t3. Quit\nEnter your choice:- ");
    scanf("%d", &choice);
    
    switch(choice){
        case 1:
            min_heap_operations();
            break;
        case 2:
            max_heap_operations();
            break;
        case 3:
            printf("\n***************\tEXITING\t***************\n");
            break;
        default:
            printf("Invalid Choice!!!");
    }

    getch();
    return 0;
}

void min_heap_operations(){
    int heapArray[50];
    int choice;
    // No element to be present at position zero as position zero can't have a left child
    heapArray[0] = -1;
    do{
        int pos, max, value, key;
        printf("\n\n***************\t BINARY MIN HEAP \t***************\n");
        printf("Choose your operation:-\n\t1. Insert in Min Heap\n\t2. Delete from Min Heap\n\t3. Search element in Min Heap\n\t4. Decrease Key\n\t");
        printf("5. Get Minimum Element\n\t6. Heapify\n\t7. Quit\nEnter your choice:- ");
        scanf("%d", &choice);
        
        switch(choice){
            case 1:
                insert_heap(heapArray, "Min Heap");
                printf("\nMIN Heap after Insertion...\n");
                for(int loopVar = 1; loopVar<heapSize; loopVar++)
                    printf("\tHeap[%d] = %d", loopVar, heapArray[loopVar]);
                break;
            case 2:
                value = delete_heap(heapArray, "Min Heap");
                printf("\nMIN Heap after Deletion...\n");
                for(int loopVar = 1; loopVar<heapSize; loopVar++)
                    printf("\tHeap[%d] = %d", loopVar, heapArray[loopVar]);
                break;
            case 3:
                printf("\nEnter the value to be searched:- ");
                scanf("%d", &value);
                pos = search_heap(heapArray, value);
                if(pos == -1)
                    printf("\nError:- Entered Element is not present in the Min Heap.");
                else
                    printf("\nResult:- Entered element is found at position %d.", pos);
                break;
            case 4:
                printf("\nEnter the value of node that is to be decreased:- ");
                scanf("%d", &value);
                printf("\nEnter the new value of node:- ");
                scanf("%d", &key);
                decrease_key(heapArray, value, key);
                printf("\nMIN Heap after Deletion...\n");
                for(int loopVar = 1; loopVar<heapSize; loopVar++)
                    printf("\tHeap[%d] = %d", loopVar, heapArray[loopVar]);
                break;
            case 5:
                value = get_minimum(heapArray);
                if(value != -1)
                    printf("\nMinimum value in the Min Heap = %d.", value);
                break;
            case 6:
                Heapify(heapArray, "Min Heap");
                break;
            case 7:
                // Quit Program
                break;
            default:
                printf("Invalid Choice!!!");
        }
    }while(choice != 7);
}

void max_heap_operations(){
    int heapArray[MAX];
    int choice;
    // No element to be present at position zero as position zero can't have a left child
    heapArray[0] = -1;
    do{
        int pos, min, value, key;
        printf("\n\n***************\t BINARY MIN HEAP \t***************\n");
        printf("Choose your operation:-\n\t1. Insert in Max Heap\n\t2. Delete from Max Heap\n\t3. Search element in Max Heap\n\t4. Increase Key\n\t");
        printf("5. Get Maximum Element\n\t6. Heapify\n\t7. Quit\nEnter your choice:- ");
        scanf("%d", &choice);
        
        switch(choice){
            case 1:
                insert_heap(heapArray, "Max Heap");
                printf("\nMAX Heap after Insertion...\n");
                for(int loopVar = 1; loopVar<heapSize; loopVar++)
                    printf("\nHeap[%d] = %d", loopVar, heapArray[loopVar]);
                break;
            case 2:
                value = delete_heap(heapArray, "Max Heap");
                printf("\nMAX Heap after Deletion...\n");
                for(int loopVar = 1; loopVar<heapSize; loopVar++)
                    printf("\nHeap[%d] = %d", loopVar, heapArray[loopVar]);
                break;
            case 3:
                printf("\nEnter value to be searched:- ");
                scanf("%d", &value);
                pos = search_heap(heapArray, value);
                if(pos == -1)
                    printf("\nError:- Entered No. is not present in the Heap.");
                else
                    printf("\nResult:- %d is found at index %d.", heapArray[pos], pos);
            case 4:
                printf("\nEnter the value of node that is to be decreased:- ");
                scanf("%d", &value);
                printf("\nEnter the new value of node:- ");
                scanf("%d", &key);
                increase_key(heapArray, value, key);
                break;
            case 5:
                value = get_maximum(heapArray);
                if(value != -1)
                    printf("\nMaximum value in the Min Heap = %d.", value);
                break;
            case 6:
                Heapify(heapArray, "Max Heap");
                break;
            case 7:
                printf("\n***************\tEXITING\t***************\n");
                break;
            default:
                printf("Invalid Choice!!!");
        }
    }while(choice != 7);
}

void insert_heap(int heap[], char* type){
    if(type == "Min Heap"){
        if(heapSize == MAX)
            printf("\nOVERFLOW Error!!!");
        else{
            int value;
            printf("Enter the No. to be inserted:- ");
            scanf("%d", &value);
            if(heapSize == 1){
                // No Elements in the Heap
                heap[1] = value;
                heapSize++;
            }
            else{
                int parent;
                int position = heapSize++;
                heap[position] = value;
                while(position > 1){
                    parent = position/2;
                    printf("\nParent(%d) = %d", parent, heap[parent]);
                    if(heap[parent] <= heap[position])
                        break;
                    else{
                        int temporary;
                        temporary = heap[parent];
                        heap[parent] = heap[position];
                        heap[position] = temporary;
                    }
                    position = parent;
                }
            }
        }
    }
    else if(type == "Max Heap"){
        if(heapSize == MAX)
            printf("\nOVERFLOW Error!!!");
        else{
            int value;
            printf("Enter the No. to be inserted:- ");
            scanf("%d", &value);
            if(heapSize == 1){
                heap[1] = value;
                heapSize++;
            }
            else{
                int parent;
                int position = heapSize++;
                heap[position] = value;
                while(position > 1){
                    parent = position/2;
                    printf("\nParent(%d) = %d", parent, heap[parent]);
                    if(heap[parent] >= heap[position])
                        break;
                    else{
                        int temporary;
                        temporary = heap[parent];
                        heap[parent] = heap[position];
                        heap[position] = temporary;
                    }
                    position = parent;
                }
            }
        }
    }
}

int delete_heap(int heap[], char* type){
    if(type == "Min Heap"){
        int deletedElement;
        if(heapSize == 0){
            printf("\nUNDERFLOW Error!!!");
        }
        else if(heapSize == 2){
            int deletedElement;
            deletedElement = heap[1];
            heap[1] == -1;
            heapSize--;
            return deletedElement;
        }
        else{
            int parent, leftChild, rightChild;
            parent = 1;
            leftChild = 2;
            rightChild = 3;
            deletedElement = heap[1];
            heap[1] = heap[heapSize-1];
            heap[--heapSize] = -1;
            while(leftChild < heapSize){
                if(leftChild != heapSize-1){
                    if(heap[parent] <= heap[leftChild] && heap[parent] <= heap[rightChild])
                        break;
                    else if(heap[parent] > heap[leftChild] && heap[parent] <= heap[rightChild]){
                        //Swap parent and leftChild
                        int temporary = heap[parent];
                        heap[parent] = heap[leftChild];
                        heap[leftChild] = temporary;
                        parent = leftChild;
                    }
                    else if(heap[parent] <= heap[leftChild] && heap[parent] > heap[rightChild]){
                        // Swap parent with rightChild
                        int temporary = heap[parent];
                        heap[parent] = heap[rightChild];
                        heap[rightChild] = temporary;
                        parent = rightChild;
                    }
                    else{
                        if(heap[rightChild] >= heap[leftChild]){
                            int temporary = heap[parent];
                            heap[parent] = heap[leftChild];
                            heap[leftChild] = temporary;
                            parent = leftChild;                     
                        }
                        else{
                            int temporary = heap[parent];
                            heap[parent] = heap[rightChild];
                            heap[rightChild] = temporary;
                            parent = rightChild;
                        }
                    }
                }
                else{
                    if(heap[parent] >= heap[leftChild]){
                        int temporary = heap[parent];
                        heap[parent] = heap[leftChild];
                        heap[leftChild] = temporary;
                        parent = leftChild;
                    }
                    else
                        parent = leftChild;
                }
                leftChild = 2*parent;
                rightChild = 2*parent+1;
                getch();
            }
            return deletedElement;
        }
    }
    else if(type == "Max Heap"){
        if(heapSize == 0){
            printf("\nUNDERFLOW Error!!!");
        }
        else if(heapSize == 1){
            int deletedElement;
            deletedElement = heap[1];
            heap[1] == -1;
            heapSize--;
            return deletedElement;
        }
        else{
            int deletedElement;
            int parent, leftChild, rightChild;
            parent = 1;
            leftChild = 2;
            rightChild = 3;
            deletedElement = heap[1];
            heap[1] = heap[heapSize-1];
            heapSize--;
            while(leftChild < heapSize){
                if(leftChild != heapSize-1){
                    if(heap[parent] >= heap[leftChild] && heap[parent] >= heap[rightChild])
                        break;
                    else if(heap[parent] < heap[leftChild] && heap[parent] >= heap[rightChild]){
                        int temporary = heap[parent];
                        heap[parent] = heap[leftChild];
                        heap[leftChild] = temporary;
                        parent = leftChild;
                    }
                    else if(heap[parent] >= heap[leftChild] && heap[parent] < heap[rightChild]){
                        int temporary = heap[parent];
                        heap[parent] = heap[rightChild];
                        heap[rightChild] = temporary;
                        parent = rightChild;
                    }
                    else{
                        if(heap[rightChild] <= heap[leftChild]){
                            int temporary = heap[parent];
                            heap[parent] = heap[leftChild];
                            heap[leftChild] = temporary;
                            parent = leftChild;
                        }
                        else{
                            int temporary = heap[parent];
                            heap[parent] = heap[rightChild];
                            heap[rightChild] = temporary;
                            parent = rightChild;
                        }
                    }
                }
                else{
                    if(heap[parent] >= heap[leftChild]){
                        printf("\nBeforeSwap:- \n\tParent(%d) = %d", parent, heap[parent]);
                        printf("\tLeftChild(%d) = %d", leftChild, heap[leftChild]);
                        int temporary = heap[parent];
                        heap[parent] = heap[leftChild];
                        heap[leftChild] = temporary;
                        printf("\nAfterSwap:- \n\tParent(%d) = %d", parent, heap[parent]);
                        printf("\tLeftChild(%d) = %d", leftChild, heap[leftChild]);
                        parent = leftChild;
                    }
                    else
                        parent = leftChild;
                }
                leftChild = 2*parent;
                rightChild = 2*parent+1;
            }
            return deletedElement;
        }
    }
}

int search_heap(int heap[], int key){
    for(int loopVar = 1; loopVar<=heapSize; loopVar++){
        if(heap[loopVar] == key)
            return loopVar;
    }
    return -1;
}

void decrease_key(int heap[], int value, int key){ 
    int position = search_heap(heap, value);
    if(position != -1){
        heap[position] = key;
        int parent;
        while(position > 1){
            parent = position/2;
            if(heap[position] > heap[parent])
                break;
            else if(heap[position] <= heap[parent]){
                    int temporary;
                    temporary = heap[parent];
                    heap[parent] = heap[position];
                    heap[position] = temporary;
            }
                position = parent;
        }
    }
    else
        printf("\nError:- value not present in Binary Heap!!!");
}

void increase_key(int heap[], int value, int key){
    int position = search_heap(heap, value);
    if(position != -1){
        heap[position] = key;
        int parent;
        while(position > 1){
            parent = position/2;
            if(heap[position] <= heap[parent])
                break;
            else if(heap[position] > heap[parent]){
                int temporary;
                temporary = heap[parent];
                heap[parent] = heap[position];
                heap[position] = temporary;
            }
            position = parent;
        }
    }
    else
        printf("\nError:- value not present in Binary Heap!!!");
}

int get_minimum(int minHeap[]){
    if(heapSize == 1){
        printf("\nError:- Heap is EMPTY!!!");
        return -1;
    }
    else
        return minHeap[1];
}

int get_maximum(int maxHeap[]){
    if(heapSize == 1){
        printf("\nError:- Heap is EMPTY!!!");
        return -1;
    }
    else
        return maxHeap[1];
}

void Heapify(int heap[], char* type){
    if(type == "Min Heap"){
        if(heapSize == 1)
            printf("\nError:- Empty Heap!!!");
        else if(heapSize == 2)
            printf("\nError:- Only One Element in the list");
        else{
            int arraySize = heapSize;
            int sortArray[MAX];
            sortArray[0] = -1;
            for(int loopVar = 1; loopVar <= arraySize;loopVar++)
                sortArray[loopVar] = delete_heap(heap, type);
            printf("\nHeapified (Sorted Heap Array) = ");
            for(int loopVar = 1; loopVar<=arraySize-1; loopVar++)
                printf("%d  ", sortArray[loopVar]);
        }
    }
    else if(type == "Max Heap"){
        if(heapSize == 1)
            printf("\nError:- Empty Heap!!!");
        else if(heapSize == 2)
            printf("\nError:- Only One Element in the list");
        else{
            int arraySize = heapSize;
            int sortArray[MAX];
            sortArray[0] = -1;
            for(int loopVar = arraySize-1; loopVar >= 1;loopVar--){
                printf("\nIteration %d\n", arraySize-loopVar);
                sortArray[loopVar] = delete_heap(heap, type);
            }
            printf("\nHeapified (Sorted Heap Array) = ");
            for(int loopVar = 1; loopVar<=arraySize-1; loopVar++)
                printf("%d  ", sortArray[loopVar]);
        }
    }
}
