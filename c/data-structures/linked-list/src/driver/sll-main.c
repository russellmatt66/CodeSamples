#include <stdlib.h>

#include "sll.h"

int main(int argc, char* argv[]){ // Test out the linked list library
    int val = 3;
    printf("Creating head with %d\n", val);
    ListNode* head = createNode(val);
    printList(head);

    val = 4;
    printf("Adding %d to the end\n", val);
    insertAtEnd(head, val);

    val = 6;
    printf("Adding %d to the beginning\n", val);
    insertAtBeginning(head, val);

    printList(head);

    deleteList(head);
    printList(head);

    printf("Freeing head\n");
    free(head); // printList only deletes all the non-head entries
    return 0;
}