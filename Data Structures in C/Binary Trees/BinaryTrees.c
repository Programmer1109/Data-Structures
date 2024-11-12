#include<stdio.h>
#include<conio.h>

struct BinaryTreeNode{
    int data;
    struct BinaryTreeNode* leftChild;
    struct BinaryTreeNode* rightChild;
};

struct BinaryTreeNode* root = NULL;

// Operations to be performed on Binary Tree
struct BinaryTreeNode* create(struct BinaryTreeNode* );
struct BinaryTreeNode* insertion(struct BinaryTreeNode* );
struct BinaryTreeNode* deletion(struct BinaryTreeNode* , int );
struct BinaryTreeNode* searching(struct BinaryTreeNode* , int );
struct BinaryTreeNode* deleteTree(struct BinaryTreeNode* );
struct BinaryTreeNode* get_deepest_node(struct BinaryTreeNode* );
struct BinaryTreeNode* delete_deepest_node(struct BinaryTreeNode* , struct BinaryTreeNode* );

// Tree Traversal Functions
void preorder_traversal(struct BinaryTreeNode* );
void inorder_traversal(struct BinaryTreeNode* );
void postorder_traversal(struct BinaryTreeNode* );

int main(){
    printf("\n***************  BINARY SEARCH TREE iMPLEMENTATION IN C ***************");
    int option;

    do{
        struct BinaryTreeNode* node = NULL;
        int value;
        printf("\n\n***************  MAIN MENU ***************\n");
        printf("\nChoose your operation:-\n\t1. Insert element in BST\n\t2. Delete element from BST\n\t3. Search element in BST");
        printf("\n\t4. Delete Binary Tree\n\t5. Pre-Order Traversal\n\t6. In-Order Traversal\n\t7. Post-Order Traversal\n\t8. Quit\nEnter your choice:- ");
        scanf("%d", &option);

        switch(option){
            case 1:
                node = create(node);
                if (node != NULL)
                    root = insertion(root, node->data);
                else
                    printf("\nError:- Couldn't allocate space for node!!!\n");
                break;
            case 2:
                printf("Enter the value of the node to be deleted:- ");
                scanf("%d", &value);
                node = searching(root, value);
                if (node != NULL)
                    root = deletion(root, value);
                else
                    printf("\nError:- Node is not present in the BST!!!");
                break;
            case 3:
                printf("Enter value of element to be be searched:- ");
                scanf("%d", &value);
                node = searching(root, value);
                if(node == NULL)
                    printf("\nResult:- Entered Element is not present in the Tree.");
                else
                    printf("\nlResult:- Entered element found in the Tree.");
                break;
            case 4:
                printf("\nDeleting entire Binary Tree");
                root = deleteTree(root);
                break;
            case 5:
                preorder_traversal(root);
                printf("\nPre-Order Traversal:- ");
                break;
            case 6:
                inorder_traversal(root);
                printf("\nIn-order Traversal:- ");
                break;
            case 7:
                postorder_traversal(root);
                printf("\nPost-Order Traversal:- ");
                break;
            case 8:
                printf("\nDeleting entire Binary Tree");
                root = deleteTree(root);
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

struct BinaryTreeNode* create(struct BinaryTreeNode* newNode){
    newNode = (struct BinaryTreeNode* ) malloc(sizeof(struct BinaryTreeNode));

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

struct BinaryTreeNode* insertion(struct BinaryTreeNode* newNode){
    if (root == NULL)
        root = newNode;
    else{
        struct BinaryTreeNode* temp = NULL;
        struct BinaryTreeNode* queue[100];
        int front=-1, rear=-1;
        queue[++rear] = root;

        while(front != rear){
            temp = queue[++front];
        
            if (temp->leftChild == NULL){
                temp->leftChild = newNode;
                return root;
            }
            else
                queue[++rear] = temp->leftChild;

            if (temp->rightChild == NULL){
                temp->rightChild = newNode;
                return root;
            }
            else
                queue[++rear] = temp->rightChild;
        }

    }

    return root;
}

struct BinaryTreeNode* searching(struct BinaryTreeNode* parent, int target){
    if (root == NULL)
        return NULL;
    else{
        struct BinaryTreeNode* temp = NULL;
        struct BinaryTreeNode* queue[100];
        int front = -1, rear = -1;
        queue[++rear] = root;

        while(front != rear){
            temp = queue[++front];

            if (temp->data == target)
                return temp;
            if (temp->leftChild != NULL)
                queue[++rear] = temp->leftChild;
            if (temp->rightChild != NULL)
                queue[++rear] = temp->rightChild;
        }

        return NULL;
    }   
}

struct BinaryTreeNode* deletion(struct BinaryTreeNode* parent, int target){
    if (root == NULL){
        printf("Error:- Empty Binary Tree!!!");
        return root;
    }

    else if (root->leftChild == NULL && root->rightChild == NULL){
        free(root);
        root = NULL;
        return root;
    }
    else{
        struct BinaryTreeNode* temp = NULL;
        struct BinaryTreeNode* keyNode = NULL;
        struct BinaryTreeNode* deepestNode = NULL;
        struct BinaryTreeNode* queue[100];
        int front=-1, rear=-1;
        queue[++rear] = root;

        while(front != rear){
            temp = queue[++front];

            if (temp->data == target)
                keyNode = temp;
            if (temp->leftChild != NULL)
                queue[++rear] = temp->leftChild;
            if (temp->rightChild != NULL)
                queue[++rear] = temp->rightChild;
        }

        if (keyNode != NULL){
            deepestNode = get_deepest_node(root);
            keyNode->data = deepestNode->data;
            deepestNode = delete_deepest_node(root, deepestNode); 
        }

        return root;
    }
}

struct BinaryTreeNode* get_deepest_node(struct BinaryTreeNode* root){
    struct BinaryTreeNode* temp = NULL;
    struct BinaryTreeNode* queue[100];
    int front = -1, rear = -1;
    queue[++rear] = root;

    while(front != rear){
        temp = queue[++front];

        if (temp->leftChild != NULL)
            queue[++rear] = temp->leftChild;
        if (temp->rightChild != NULL)
            queue[++rear] = temp->rightChild;
    }

    return temp;
}

struct BinaryTreeNode*  delete_deepest_node(struct BinaryTreeNode* root, struct BinaryTreeNode* targetNode){
    struct BinaryTreeNode* temp = NULL;
    struct BinaryTreeNode* queue[100];
    int front = -1, rear = -1;
    queue[++rear] = root;

    while(front != rear){
        temp = queue[++front];

        if (temp == targetNode){
            temp = NULL;
            free(targetNode);
            return targetNode;
        }

        if (temp->rightChild != NULL){
            if (temp->rightChild == targetNode){
                temp->rightChild = NULL;
                free(targetNode);
                return targetNode;
            }
            else
                queue[++rear] = temp->rightChild;
        }

        if (temp->leftChild != NULL){
            if (temp->leftChild == targetNode){
                temp->leftChild = NULL;
                free(temp->leftChild);
                return targetNode;
            }
            else
                queue[++rear] = temp->leftChild;
        }
    }
}

struct BinaryTreeNode* deleteTree(struct BinaryTreeNode* parent){
    if(parent != NULL){
        struct BinaryTreeNode* leftNode = deleteTree(parent->leftChild);
        struct BinaryTreeNode* rightNode = deleteTree(parent->rightChild);
        printf("\nDeleted Node:- Data = %d", parent->data);
        free(parent);        
    }
    return parent;
}

void preorder_traversal(struct BinaryTreeNode* parent){
    if (parent != NULL){
        printf("\t %d", parent->data);
        preorder_traversal(parent->leftChild);
        preorder_traversal(parent->rightChild);
    }
}

void inorder_traversal(struct BinaryTreeNode* parent){
    if (parent != NULL){
        preorder_traversal(parent->leftChild);
        printf("\t %d", parent->data);
        preorder_traversal(parent->rightChild);
    }
}

void postorder_traversal(struct BinaryTreeNode* parent){
    if (parent != NULL){
        preorder_traversal(parent->leftChild);
        preorder_traversal(parent->rightChild);
        printf("\t %d", parent->data);
    }
}
