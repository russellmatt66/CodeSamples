# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle-ii/submissions/1153889028/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        node_set = set()
        # print(node_set)

        while head is not None:
            if head not in node_set:
                node_set.add(head)
            else:
                return head
            # print(node_set)
            head = head.next

        return None
