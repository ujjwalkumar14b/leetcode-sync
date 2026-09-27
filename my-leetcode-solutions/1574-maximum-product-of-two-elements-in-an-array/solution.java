class Solution {
    public int maxProduct(int[] nums) {
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for(int i = 0; i < nums.length; i++){
            pq.add(nums[i]);
        }
        
        int max = pq.remove();
        int max2 = pq.remove();
        return (max-1) * (max2 -1);
    }
}
