#include<stdio.h>
#include<conio.h>

struct BSTNode{
    int data;
    struct BSTNode* leftChild;
    struct BSTNode* rightChild;
};

// Initiallizing the Root Node
struct BSTNode* root = NULL;

// Functions to perform Basic Operations on Binary Search Tree
struct BSTNode* create_BST_Node(struct BSTNode* );
struct BSTNode* insert_BST_element(struct BSTNode* , struct BSTNode* );
struct BSTNode* delete_BST_element(struct BSTNode* , int );
struct BSTNode* delete_BST(struct BSTNode* );

// Functions to traverse a Binary Search Tree
void preOrder_Traversal(struct BSTNode* );
void inOrder_Traversal(struct BSTNode* );
void postOrder_Traversal(struct BSTNode* );

// Fucntions to search in Binary Search Tree
struct BSTNode* find_smallest_element(struct BSTNode* );
struct BSTNode* find_largest_element(struct BSTNode* );
struct BSTNode* search_BST_element(struct BSTNode* , int );

// Functions to find No. of Nodes in Binary Search Tree
int total_Nodes(struct BSTNode* );
int total_leaf_Nodes(struct BSTNode* );
int total_internal_Nodes(struct BSTNode* );

//Function to find Height of Binary Search Tree
int Height(struct BSTNode* );

//Function to find Mirror Image of Binary Search Tree
struct BSTNode* mirrorImage(struct BSTNode* );

int main(){
    printf("\n***************  BINARY SEARCH TREE iMPLEMENTATION IN C ***************");
    int option;

    do{
        struct BSTNode* node = NULL;
        int value;
        printf("\n\n***************  MAIN MENU ***************\n");
        printf("\nChoose your operation:-\n\t1. Insert element in BST\n\t2. Delete element from BST\n\t3. Search element in BST");
        printf("\n\t4. Inorder Traversal\n\t5. Post Order Traversal\n\t6. Pre Order Traversal\n\t7. Total No. of Nodes in BST");
        printf("\n\t8. No. of Leaf Nodes in BST\n\t9. No. of Internal Nodes in BST\n\t10. Height of BST\n\t11. Mirror Image of BST");
        printf("\n\t12. Minimum Element in BST\n\t13. Maximum Element in BST\n\t14. Delete Tree\n\t15. Quit\nEnter your choice:- ");
        scanf("%d", &option);

        switch(option){
            case 1:
                node = create_BST_Node(node);
                if (node != NULL)
                    root = insert_BST_element(root, node->data);
                else
                    printf("\nError:- Couldn't allocate space for node!!!\n");
                break;
            case 2:
                printf("Enter the value of the node to be deleted:- ");
                scanf("%d", &value);
                node = search_BST_element(root, value);
                if (node != NULL)
                    root = delete_BST_element(root, value);
                else
                    printf("\nError:- Node is not present in the BST!!!");
                break;
            case 3:
                printf("Enter value of element to be be searched:- ");
                scanf("%d", &value);
                node = search_BST_element(root, value);
                if(node == NULL)
                    printf("\nResult:- Entered Element is not present in the Tree.");
                else
                    printf("\nlResult:- Entered element found in the Tree.");
                break;
            case 4:
                inOrder_Traversal(root);
                break;
            case 5:
                postOrder_Traversal(root);
                break;
            case 6:
                preOrder_Traversal(root);
                break;
            case 7:
                value = total_Nodes(root);
                printf("\nResult:- Total Nodes = %d", value);
                break;
            case 8:
                value = total_leaf_Nodes(root);
                printf("\nResult:- Total Leaf Nodes = %d", value);
                break;
            case 9:
                value = total_internal_Nodes(root);
                printf("\nResult:- Total External Nodes = %d", value);
                break;
            case 10:
                value = Height(root);
                printf("\nResult:- Height of Tree = %d", value);
                break;
            case 12:
                node = find_smallest_element(root);
                printf("\nResult:- Smallest Element->\tAddress:- %x\tData:- %d", node, node->data);
                break;
            case 13:
                node = find_largest_element(root);
                printf("\nResult:- Largest Element->\tAddress:- %x\tData:- %d", node, node->data);
                break;
            case 14:
                root = delete_BST(root);
                break;
            case 15:
                root = delete_BST(root);
                break;
            default:
                printf("\nError:- Invalid Choice");
        }
        node = NULL;
        value = -1;
    }while(option != 15);
    
    getch();
    return 0;
}

// Functions to perform Basic Operations on Binary Search Tree
struct BSTNode* create_BST_Node(struct BSTNode* newNode){
    newNode = (struct BSTNode* ) malloc(sizeof(struct BSTNode));

    if(newNode == NULL)
        return NULL;
    else{
        int number;
        printf("\nEnter value of key:- ");
        scanf("%d", &number);
        newNode->data = number;
        newNode->leftChild = NULL;
        newNode->rightChild = NULL;
        printf("\nNew Node-> Address = %x\tLeft Child = %x\tData = %d\tRight Child = %x", newNode, newNode->leftChild, newNode->data, newNode->rightChild);
        return newNode;
    }
}

struct BSTNode* insert_BST_element(struct BSTNode* parent, struct BSTNode* newNode){
    if(root == NULL){
        printf("\nEMPTY Binary Search Tree...\nInserting Root Node....");
        root = newNode;
        printf("\nRoot Node-> Address = %x\tData = %d\tLeft Child = %x\tRight Child = %x", root,  root->data, root->leftChild, root->rightChild);
        return root;
    }
    else{
        printf("\nParent Node-> Address = %x\tLeft Child = %x\tData = %d\tRight Child = %x", parent, parent->leftChild, parent->data, parent->rightChild);
        printf("\nNew Node-> Address = %x\tLeft Child = %x\tData = %d\tRight Child = %x", newNode, newNode->leftChild, newNode->data, newNode->rightChild);
        if (parent == NULL)
            parent = newNode;
        else if (parent->data < newNode->data)
            parent->rightChild = insert_BST_element(parent->rightChild, newNode);
        else if (parent->data > newNode->data)
            parent->leftChild = insert_BST_element(parent->leftChild, newNode);
        else if (parent->data == newNode->data)
            printf("\nError:- Node already exists in the BST!!!\n");
        return parent;
    }
}

struct BSTNode* delete_BST_element(struct BSTNode* parent, int target){
    if(root == NULL){
        printf("Error:- Empty BST!!!");
        return NULL;
    }
    else if(target < parent->data)
        parent->leftChild = delete_BST_element(parent->leftChild, target);
    else if (target > parent->data)
        parent->rightChild = delete_BST_element(parent->rightChild, target);
    else if (target == parent->data){
        if(parent->leftChild == NULL && parent->rightChild == NULL){
            free(parent);
            return NULL;
        }
        else if(parent->leftChild == NULL && parent->rightChild != NULL){
            struct BSTNode* temp = NULL;
            temp = parent;
            parent = parent->rightChild;
            free(temp);
            return parent;
        }
        else if (parent->leftChild != NULL && parent->rightChild == NULL){
            struct BSTNode* temp = NULL;
            temp = parent;
            parent = parent->leftChild;
            free(temp);
            return parent;
        }
        else if(parent->leftChild != NULL && parent->rightChild != NULL){
            struct BSTNode* temp = NULL;
            temp = find_smallest_element(parent->rightChild);
            parent->data = temp->data;
            parent->rightChild = delete_BST_element(parent->rightChild, temp->data);
        }
    }
    return parent;
}

struct BSTNode* delete_BST(struct BSTNode* parent){
    if(parent != NULL){
        struct BSTNode* leftNode = delete_BST(parent->leftChild);
        struct BSTNode* rightNode = delete_BST(parent->rightChild);
        printf("\nDeleted Node:- Data = %d", parent->data);
        free(parent);
    }
    return parent;
}

// Fucntions to search in Binary Search Tree
struct BSTNode* find_smallest_element(struct BSTNode* parent){
    if (root == NULL || parent->leftChild == NULL)
        return parent;
    else
        return find_smallest_element(parent->leftChild);
}

struct BSTNode* find_largest_element(struct BSTNode* parent){
    if (root == NULL || parent->rightChild == NULL)
        return parent;
    else
        return find_largest_element(parent->rightChild);
}

struct BSTNode* search_BST_element(struct BSTNode* parent, int value){
    if(root==NULL || parent->data == value)
        return parent;
    else if(value > parent->data)
        return search_BST_element(parent->rightChild, value);
    else if(value < parent->data)
        return search_BST_element(parent->leftChild, value);
}

// Functions to traverse a Binary Search Tree
void preOrder_Traversal(struct BSTNode* parent){
    if (parent != NULL){
        printf("%d", parent->data);
        preOrder_Traversal(parent->leftChild);
        preOrder_Traversal(parent->rightChild);
    }
}

void inOrder_Traversal(struct BSTNode* parent){
    if (parent != NULL){
        preOrder_Traversal(parent->leftChild);
        printf("%d", parent->data);
        preOrder_Traversal(parent->rightChild);
    }
}

void postOrder_Traversal(struct BSTNode* parent){
    if (parent != NULL){
        preOrder_Traversal(parent->leftChild);
        preOrder_Traversal(parent->rightChild);
        printf("%d", parent->data);
    }
}

// Functions to find No. of Nodes in Binary Search Tree
int total_Nodes(struct BSTNode* parent){
    if (parent == NULL)
        return 0;
    else
        return (total_Nodes(parent->leftChild) + total_Nodes(parent->rightChild) + 1);
}

int total_leaf_Nodes(struct BSTNode* parent){
    if (parent == NULL)
        return 0;
    else if (parent->leftChild == NULL && parent->rightChild == NULL)
        return 1;
    else
        return (total_leaf_Nodes(parent->leftChild) + total_leaf_Nodes(parent->rightChild));
}

int total_internal_Nodes(struct BSTNode* parent){
    if(parent->leftChild == NULL && parent->rightChild == NULL)
        return 0;
    else
        return (total_external_Nodes(parent->leftChild) + total_external_Nodes(parent->rightChild) + 1);
}

// Function to find Height of Binary Search Tree
int Height(struct BSTNode* parent){
    int leftHeight, rightHeight;

    if (parent==NULL)
        return 0;
    else{
        leftHeight = Height(parent->leftChild);
        rightHeight = Height(parent->rightChild);
        if (leftHeight > rightHeight)
            return leftHeight+1;
        else
            return rightHeight+1;
    }
}

// Function to find Mirror Image of Binary Search Tree
struct BSTNode* mirrorImage(struct BSTNode* parent){
    struct BSTNode* leftNode;
    struct BSTNode* rightNode;
    struct BSTNode* temp;

    if (parent->leftChild != NULL && parent->rightChild != NULL){
        leftNode = mirror(parent->leftChild);
        rightNode = mirror(parent->rightChild);
        temp = leftNode;
        leftNode = rightNode;
        rightNode = temp;
    }
    
    return parent;
}
