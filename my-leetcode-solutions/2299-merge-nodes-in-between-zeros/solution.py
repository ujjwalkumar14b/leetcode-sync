class Solution:
  def mergeNodes(self, head: ListNode | None) -> ListNode | None:

    modify = head.next
    next_node = modify

    while next_node:
      current_sum = 0

      while next_node.val != 0:
        current_sum += next_node.val
        next_node = next_node.next

      modify.val = current_sum
      next_node = next_node.next
      modify.next = next_node
      modify = modify.next

    return head.next
