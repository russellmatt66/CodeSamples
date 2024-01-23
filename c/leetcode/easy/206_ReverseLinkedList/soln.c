/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* createLLNode(int, struct ListNode*);
void printList(struct ListNode*);

/* INCOMPLETE
 * Solution: O(N) time, O(N) space 
 * 
 * Current Task: Create linked list from array of values
 * */ 
struct ListNode* reverseList(struct ListNode* head) {
    int list_size = 0;
    struct ListNode* temp = head;
    // get the size of the list
    while (temp != NULL){
        list_size++;
        temp = temp->next; 
    }
    // printf("%d\n",list_size);
    
    int* list_vals = (int*)malloc(list_size*sizeof(int));
    temp = head;
    int il = 0;
    while (temp != NULL){
        list_vals[il] = temp->val;
        temp = temp->next;
    }

    // Need to implement code to construct linked list from an array 
    int ib = list_size - 1;
    struct ListNode* reverse_head = createLLNode(list_vals[ib], NULL);
    ib--;
    while (ib >= 0){

    }

    free(list_vals);
    free(temp);

    return reverse_head;
}

struct ListNode* createLLNode(int val, struct ListNode* next){
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (newNode != NULL){
        newNode->val = val;
        newNode->next = next;
    }
    return newNode;
}

void printList(struct ListNode* head){
    while (head != NULL){
        int node = 0;
        printf("Value at node %d is %d", node, head->val);
        head = head->next;
    }
    return;
}
