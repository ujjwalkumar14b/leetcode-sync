import java.util.Arrays;

class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        int n = nums.length;
        int[][] paired = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            paired[i][0] = nums[i];
            paired[i][1] = i;
        }
        
        Arrays.sort(paired, (a, b) -> Integer.compare(b[0], a[0]));        
        Arrays.sort(paired, 0, k, (a, b) -> Integer.compare(a[1], b[1]));
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = paired[i][0];
        }
        return result;
    }
}
