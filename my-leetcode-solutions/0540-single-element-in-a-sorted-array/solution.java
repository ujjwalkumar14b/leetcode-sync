class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Ensure mid is even (so we can compare with mid+1)
            if (mid % 2 == 1) {
                mid--;
            }

            if (nums[mid] == nums[mid + 1]) {
                // Single element is to the right
                left = mid + 2;
            } else {
                // Single element is to the left (or at mid)
                right = mid;
            }
        }

        return nums[left];
    }
}

