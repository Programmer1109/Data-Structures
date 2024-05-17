#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
 
#define MAX 100

char stack[100];
int stackIndex = -1;

// Function to return precedence of operators
int precedence(char c) {
    if (c == '^')
        return 3;
    else if (c == '/' || c == '*')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}
 
// Function to return associativity of operators
char associativity(char c) {
    if (c == '^')
        return 'R';
    return 'L'; // Default to left-associative
}
 
void push(char value){
    printf("\n%c", value);
    if(stackIndex == MAX-1)
        printf("\nError:- OVERFLOW ERROR\n");
    else{
        stackIndex++;
        stack[stackIndex] = value;
        printf("\nSTACK = %s\tStack Index = %d", stack, stackIndex);
    }
}

char pop(){
    if(stackIndex == -1)
        printf("\nError:- UNDERFLOW ERROR!!!\n");
    else{
        char value = stack[stackIndex];
        stackIndex--;
        printf("\nSTACK = %s\tStack Index = %d", stack, stackIndex);
        return value;
    }
}

// The main function to convert infix expression to postfix expression
char* infixToPostfix(char source[]) {
    printf("\nSource = %s\n", source);
    static char result[100];
    int resultIndex = 0;
    int len = strlen(source);
    //int stackIndex = -1;
    
    printf("\nSource = %s", source);
    for(int sourceIndex = 0; sourceIndex < len; sourceIndex++){
        printf("\n**************************************\n");
        // character = an operand, add it to the output string.
        if ((source[sourceIndex] >= 'a' && source[sourceIndex] <= 'z') || (source[sourceIndex] >= 'A' && source[sourceIndex] <= 'Z') || (source[sourceIndex] >= '0' && source[sourceIndex] <= '9')) {
            printf("\nSource = %c", source[sourceIndex]);
            result[resultIndex] = source[sourceIndex];
            resultIndex++;
            printf("\nresult[%d]= %s", resultIndex, result);
        }
        // character =  '(', push it to the stack.
        else if (source[sourceIndex] == '(') {
            printf("\nSource = %c", source[sourceIndex]);
            push(source[sourceIndex]);
        }
        // Icharacter = ')', pop and add to the output string from the stack until an '(' is encountered.
        else if (source[sourceIndex] == ')') {
            printf("\nSource = %c", source[sourceIndex]);
            while (stackIndex >= 0 && stack[stackIndex] != '(') {
                result[resultIndex++] = pop();
            }
            stackIndex--; // Pop '('
        }
        // character = operator, check for it's precedence and  
        else if(source[sourceIndex] == '*' || source[sourceIndex] == '+' || source[sourceIndex] == '-' || source[sourceIndex] == '/' || source[sourceIndex] == '%'){
            printf("\nSource = %c", source[sourceIndex]);
            while (stackIndex != -1 && (precedence(source[sourceIndex]) < precedence(stack[stackIndex]) || precedence(source[sourceIndex]) == precedence(stack[stackIndex]) &&
                                        associativity(source[sourceIndex]) == 'L')) {
                result[resultIndex++] = pop();
            }
            push(source[sourceIndex]);
        }
    }
 
    // Pop all the remaining elements from the stack
    while (stackIndex >= 0) {
        result[resultIndex++] = pop();
    }
 
    result[resultIndex] = '\0';
    printf("\n%s\n", result);
    return result;
}
 
char* infixToPrefix(char infix[]){
    //Reverse the infix string expression
    char* myString; 
    static char result[100];
    int loopVar = 0;
    int stringLength = strlen(infix);
    myString = (char *) malloc(stringLength * 2 * sizeof(char));
    printf("\nLength = %d", stringLength);
    //printf("\nmyString = %s", myString);
    printf("\nREVERSING STRING...");
    while(loopVar < stringLength){
        myString[loopVar] = infix[stringLength-1-loopVar];
        if(myString[loopVar] == '(')
            myString[loopVar] = ')';
        else if(myString[loopVar] == ')')
            myString[loopVar] = '(';
        printf("\nloopvar = %d\tmystring front = %c\tinfix rear = %c", loopVar, myString[loopVar], infix[stringLength-1-loopVar]);
        loopVar++;
    }
    printf("\nmyString = %s", myString);

    // Compute the Postfix expression of the String
    myString = infixToPostfix(myString);

    // Reverse the postfix string to find the prefix string
    loopVar = 0;
    printf("\nLength = %d", stringLength);
    printf("\nmyString = %s", myString);
    printf("\nREVERSING STRING...");
    while(loopVar < stringLength){
        result[loopVar] = myString[stringLength-1-loopVar];
        if(result[loopVar] == '(')
            result[loopVar] = ')';
        else if(result[loopVar] == ')')
            result[loopVar] = '(';
        printf("\nloopvar = %d\tresult front = %c\tmystring rear = %c", loopVar, result[loopVar], myString[stringLength-1-loopVar]);
        loopVar++;
    }
    printf("\nmyString = %s", myString);
    return result;
}

int main() {
    char expression[100];
    char* prefix;
 
    // Function call
    printf("Enter Infix Expression:- ");
    scanf("%s", expression);
    prefix = infixToPrefix(expression);
    printf("\nPrefix Expression:- %s\n", prefix);
    
    getch();
    return 0;
}
