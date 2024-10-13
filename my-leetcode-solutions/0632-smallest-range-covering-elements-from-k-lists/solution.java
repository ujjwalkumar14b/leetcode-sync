import java.util.*;

class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        
        int max = Integer.MIN_VALUE;
        
        for (int i = 0; i < nums.size(); i++) {
            minHeap.offer(new int[]{nums.get(i).get(0), i, 0});
            max = Math.max(max, nums.get(i).get(0)); // Track the maximum element
        }
        
        int start = minHeap.peek()[0]; // Initial smallest range start
        int end = max; // Initial smallest range end
        int rangeStart = start; // The best range start
        int rangeEnd = end; // The best range end
        
        while (true) {
            int[] minEntry = minHeap.poll();
            int minValue = minEntry[0];
            int listIndex = minEntry[1];
            int elementIndex = minEntry[2];
            
            if (max - minValue < rangeEnd - rangeStart || 
               (max - minValue == rangeEnd - rangeStart && minValue < rangeStart)) {
                rangeStart = minValue;
                rangeEnd = max;
            }            
            if (elementIndex + 1 >= nums.get(listIndex).size()) {
                break;
            }
            int nextValue = nums.get(listIndex).get(elementIndex + 1);
            minHeap.offer(new int[]{nextValue, listIndex, elementIndex + 1});
            max = Math.max(max, nextValue); 
        }
        
        return new int[]{rangeStart, rangeEnd};
    }
}

