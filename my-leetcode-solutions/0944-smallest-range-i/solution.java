class Solution {
    public int smallestRangeI(int[] nums, int k) {
        
        int minVal = nums[0];
        int maxVal = nums[0];
        
        for (int num : nums) {
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
        }
        return Math.max(0, maxVal - minVal - 2 * k);
    }
}
