class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0; // position for the next non-zero number

        // Move all non-zero numbers forward
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[j] = nums[i];
                j++;
            }
        }

        // Fill remaining positions with zero
        while (j < nums.length) {
            nums[j] = 0;
            j++;
        }
    }
}

