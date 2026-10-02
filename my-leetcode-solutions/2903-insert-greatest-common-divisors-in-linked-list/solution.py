class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)            
            gcd_node = ListNode(gcd_val, curr.next)
            curr.next = gcd_node            
            curr = gcd_node.next
            
        return head
