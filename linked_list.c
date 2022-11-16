#include <stdio.h>
#include <stdlib.h>
#include <time.h>

    struct Node {
        int data; 
        struct Node *next;
    };

int main() {

    srand(time(NULL));
    int random;
    struct Node *primaryNode = NULL, *previousNode = NULL, *headNode = NULL;
    
    headNode = malloc(sizeof(struct Node));
    if(headNode == NULL) {
        return 1;
    }
    headNode->data = rand() % 36;
    headNode->next = NULL;

    previousNode = headNode;
    
    while(random != 35) {
        
        random = rand() % 36;
        if(random == 35) {
            break;
        }
        
        primaryNode = malloc(sizeof(struct Node));
        if(primaryNode == NULL) {
            return 1;
        }
        primaryNode->data = random;
        
        previousNode->next = primaryNode;
        previousNode = primaryNode;
        
    }
    
    primaryNode = headNode;
    
    printf("Printing full linked list: \n");
    while(primaryNode != NULL) {
        printf("%d\n", primaryNode->data);
        previousNode = primaryNode;
        primaryNode = primaryNode->next;
        free(previousNode);
    }
    return 0;
}
