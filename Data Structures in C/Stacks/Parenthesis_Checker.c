#include<stdio.h>

#define MAX 50

int topIndex = -1;
short int flag = -1;
char stackArray[MAX];

void push_stack(char );
void pop_stack(char );

int main(){
    char inputString[30] ;
    char exitFlag;

    do{
        printf("Enter the expression:- ");
        fflush(stdin);
        scanf("%s", inputString);
        printf("Input String = %s\n", inputString);

        printf("TEST STATEMENT!!!\n");
        for(int i=0; inputString[i] != '\0'; i++){
            if(*(inputString+i) == '(' || *(inputString+i) == '[' || *(inputString+i) == '{'){
                printf("\n Performing push...\n");
                push_stack(*(inputString+i));
            }
            else if(*(inputString+i) == ')' || *(inputString+i) == ']' || *(inputString+i) == '}'){
                if(topIndex == -1)
                    flag = 1;
                else{
                    printf("\nPerforming Pop...\n");
                    pop_stack(*(inputString+i));
                }
            }
        }

        if(strlen(inputString) != 0){
            if(topIndex == -1 && flag == 0)
                printf("\nResult:- Entered Expression is balanced!!!");
            else
                printf("\nResult:- Entered Expression is not balanced!!!");
        }
        else
            printf("\nError:- Input String is Empty.\n\t Please ENTER an EXPRESSION!!!\n");
        printf("\n************ PRESS X TO EXIT ************");
        fflush(stdin);
        scanf("%c", &exitFlag);
        topIndex = -1;
    }while(exitFlag != 'x');
    return 0;
}

void push_stack(char element){
    printf("\nTop = %d\telement = %c\n", topIndex, stackArray[topIndex]);
    if(topIndex==MAX-1)
        printf("OVERFLOW ERROR!!!\n");
    else
        stackArray[++topIndex] = element;
    printf("\nTop = %d\telement = %c\n", topIndex, stackArray[topIndex]);
}

void pop_stack(char currentElement){
    if(topIndex == -1)
        printf("UNDERFLOW ERROR!!!\n");
    else{
        printf("\nTop = %d\tprevious element = %c\tcurrent Element = %c\n", topIndex, stackArray[topIndex], currentElement);
        if(stackArray[topIndex] == '(' && currentElement == ')')
            topIndex--;
        else if(stackArray[topIndex] == '[' && currentElement == ']')
            topIndex--;
        else if(stackArray[topIndex] == '{' && currentElement == '}')
            topIndex--;
        printf("\nTop = %d", topIndex);
    }
}
