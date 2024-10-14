import java.util.PriorityQueue;

class Solution {
    public long maxKelements(int[] nums, int k) {
        // Create a max-heap using a priority queue
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        
        // Add all elements to the max-heap
        for (int num : nums) {
            maxHeap.add(num);
        }
        
        long score = 0;

        // Perform k operations
        for (int i = 0; i < k; i++) {
            // Extract the maximum element
            int maxValue = maxHeap.poll();
            score += maxValue;

            // Calculate the new value after the operation
            int newValue = (int) Math.ceil(maxValue / 3.0);
            
            // Push the new value back into the heap
            maxHeap.add(newValue);
        }

        return score;
    }

}

