import java.util.*;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int i = 0; i < m; i++) {
            minHeap.offer(nums1[i]);
        }
        for (int j = 0; j < n; j++) {
            minHeap.offer(nums2[j]);
        }

        int index = 0;
        while (!minHeap.isEmpty()) {
            nums1[index++] = minHeap.poll();
        }
    }
}

