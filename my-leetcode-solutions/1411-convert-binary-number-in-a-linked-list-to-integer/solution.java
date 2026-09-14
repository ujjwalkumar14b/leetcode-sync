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
    public int getDecimalValue(ListNode head) {
        
        String binaryString = "";
        ListNode temp = head;
        
        while(temp != null){
            binaryString += temp.val;
            temp = temp.next;
        }
        return Integer.parseInt(binaryString, 2);
    }
}
