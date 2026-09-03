import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        Set<Integer> window = new HashSet<>();
        if (nums == null || nums.length <= 1 || k <= 0) {
            return false;
        }
        for (int i = 0; i < nums.length; i++) {
            if (window.contains(nums[i])) {
                return true;
            }            
            window.add(nums[i]);            
            if (window.size() > k) {
                window.remove(nums[i - k]);
            }
        }
        return false;
    }
}

