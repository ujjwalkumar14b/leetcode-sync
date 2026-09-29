class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []

        while l1:
            s1.append(str(l1.val))
            l1 = l1.next

        while l2:
            s2.append(str(l2.val))
            l2 = l2.next

        num1 = int("".join(s1[::-1]))
        num2 = int("".join(s2[::-1]))
        total_str = str(num1 + num2)[::-1] 

        dummy = ListNode(0)
        curr = dummy
        for char in total_str:
            curr.next = ListNode(int(char))
            curr = curr.next

        return dummy.next

        
