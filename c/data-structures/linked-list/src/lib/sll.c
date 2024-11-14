#include <stdio.h>
#include <stdlib.h>

#include "sll.h"

// No tail, just head

int getVal(const int n, ListNode* head){
    int i = 0;
    ListNode* temp = head;
    while (i < n && temp != NULL){
        temp = temp->next;
        i++;
    }

    if (i > n || temp == NULL){
        printf("Requested value is out-of-bounds\n");
        return head->val;
    }

    return temp->val;
}

ListNode* createNode(const int val){
    ListNode* new_node = (ListNode*)malloc(sizeof(ListNode));
    
    new_node->next = NULL;
    new_node->val = val;
    
    return new_node;
}

// O(N) - no tail
void insertAtEnd(ListNode* head, const int val){
    ListNode* new_node = createNode(val);
    ListNode* temp = head;
    
    while (temp->next != NULL){
        temp = temp->next;
    }
    
    temp->next = new_node;
    return;
}

void insertAtBeginning(ListNode* head, const int val){
    ListNode* new_node = createNode(val);
    ListNode* temp = head->next;

    head->next = new_node;
    new_node->next = temp;
    
    return;
}

void deleteNode(ListNode** head, ListNode* dead_node){
    if (*head == NULL || dead_node == NULL){
        return;
    }

    if (*head == dead_node){
        *head = dead_node->next; 
        free(dead_node);
        return;
    }

    ListNode* temp = *head;
    while (temp->next != dead_node && temp->next != NULL){
        temp = temp->next;
    }

    if (temp->next == NULL){ // not found
        return;
    }

    temp->next = dead_node->next;
    free(dead_node);
    return;
}

void printList(ListNode* head){
    if (head == NULL){
        printf("List is empty\n");
        return;
    }

    ListNode* temp = head;
    int i = 0;
    printf("Printing list\n");
    while (temp->next != NULL){
        printf("Node %d, val = %d\n", i, temp->val);
        temp = temp->next;
        i++;
    }
    printf("Node %d, val = %d\n", i, temp->val);

    return;
}

void deleteList(ListNode* head){
    printf("Deleting list\n");
    while (head->next != NULL){
        deleteNode(&head, head->next);
    }
    printf("List deleted\n");
    return;
}