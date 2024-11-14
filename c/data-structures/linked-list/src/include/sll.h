#include <stdio.h>

typedef struct ListNode{
    struct ListNode* next;
    int val;
} ListNode;

int getVal(const int n, ListNode* head);
ListNode* createNode(const int val);
void insertAtEnd(ListNode* head, const int val);
void insertAtBeginning(ListNode* head, const int val);
void deleteNode(ListNode** head, ListNode* dead_node);
void printList(ListNode* head);
void deleteList(ListNode* head);