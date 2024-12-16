#ifndef DLL_H
#define DLL_H

#include <stdio.h>

typedef struct ListNode{
    ListNode* prev;
    ListNode* next;
    int val;
} ListNode; 

int getVal(const int n, ListNode* head);
ListNode* createNode(const int val);
void insertAtEnd(const ListNode* tail, const int new_val);
void insertAtBeginning(const ListNode* head, const int new_val);
void deleteNode(ListNode* head, ListNode* dead_node);
void printListForward(ListNode* head);
void printListBackward(ListNode* tail);
void deleteList(ListNode* head);

#endif