import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public List<Integer> findMissingElements(int[] nums) {

        int minNumber = Integer.MAX_VALUE;
        int maxNumber = Integer.MIN_VALUE;
        HashSet<Integer> set = new HashSet<>();
        List<Integer> missingNumber = new ArrayList<>();
        
        if (nums == null || nums.length == 0) {
            return missingNumber;
        }
        for (int num : nums) {
            minNumber = Math.min(num, minNumber);
            maxNumber = Math.max(num, maxNumber);
            set.add(num);
        }
        for (int i = minNumber + 1; i < maxNumber; i++) {
            if (!set.contains(i)) {
                missingNumber.add(i);
            }
        }
        return missingNumber;
    }
}

