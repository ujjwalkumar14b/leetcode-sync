/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode temp = head;
        while (temp != null) {
            size++;
            temp = temp.next;
        }

        // If the node to remove is the head
        if (n == size) {
            return head.next;
        }

        // Second pass: go to (size - n - 1)th node
        int index = 0;
        ListNode current = head;
        while (index < size - n - 1) {
            current = current.next;
            index++;
        }

        // Skip the nth node from the end
        current.next = current.next.next;

        return head;
    }
}

