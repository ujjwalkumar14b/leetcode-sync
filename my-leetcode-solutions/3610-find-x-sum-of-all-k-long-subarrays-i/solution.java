class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] answer = new int[n - k + 1];
        
        // Sliding window approach
        for (int i = 0; i <= n - k; i++) {
            // Create a subarray of length k
            int[] subarray = Arrays.copyOfRange(nums, i, i + k);
            answer[i] = calculateXSum(subarray, x);
        }
        
        return answer;
    }
    
    private int calculateXSum(int[] subarray, int x) {
        // Count frequencies of elements in the subarray
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : subarray) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        // Create a priority queue to find top x elements based on frequency and value
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? b[1] - a[1] : b[0] - a[0]
        );
        
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            maxHeap.offer(new int[]{entry.getValue(), entry.getKey()});
        }
        
        // Calculate the x-sum from the top x elements
        int xSum = 0;
        for (int i = 0; i < x && !maxHeap.isEmpty(); i++) {
            int[] topElement = maxHeap.poll();
            int frequency = topElement[0];
            int value = topElement[1];
            xSum += frequency * value;
        }
        
        return xSum;
    }
}

