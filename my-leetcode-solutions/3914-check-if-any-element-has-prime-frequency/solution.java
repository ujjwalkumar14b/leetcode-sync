import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            frequency.put(nums[i], frequency.getOrDefault(nums[i], 0) + 1);
        }        
        for (int count : frequency.values()) {
            if (isPrime(count)) {
                return true;
            }
        }
        return false;
    }
    
    // Helper method to check if a number is prime
    private boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
