# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Temporarily store next node
            curr.next = prev # Reverse current node's pointer
            prev = curr      # Move prev pointer 1 step forward
            curr = nxt       # Move curr pointer 1 step forward
            
        return prev
        
