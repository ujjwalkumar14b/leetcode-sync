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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0); // Dummy node to help build the result
        ListNode current = dummyHead; // Pointer to build the result list
        int carry = 0; // To store carry during addition

        // Traverse both lists
        while (l1 != null || l2 != null) {
            int sum = carry; // Start with carry

            if (l1 != null) {
                sum += l1.val; // Add value from l1 if available
                l1 = l1.next; // Move to the next node
            }
            if (l2 != null) {
                sum += l2.val; // Add value from l2 if available
                l2 = l2.next; // Move to the next node
            }

            carry = sum / 10; // Calculate new carry
            current.next = new ListNode(sum % 10); // Create new node with the digit
            current = current.next; // Move the current pointer forward
        }

        // If there's any carry left, add a new node
        if (carry > 0) {
            current.next = new ListNode(carry);
        }

        // The result list starts from the next node of the dummy head
        return dummyHead.next;
    }
}

