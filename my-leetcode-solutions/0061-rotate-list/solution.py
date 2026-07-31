# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate list length and locate the last node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Connect tail to head to form a circular list
        tail.next = head
        
        # Find the split point 
        k = k % length
        steps_to_new_tail = length - k - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # Break the circle and return the new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
