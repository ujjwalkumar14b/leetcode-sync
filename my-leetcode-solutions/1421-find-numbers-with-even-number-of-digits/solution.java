class Solution {
    public int findNumbers(int[] nums) {
        
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            int countDigits = 0;
            while(nums[i] > 0){
                int rem = nums[i] % 10;
                countDigits++;
                nums[i] /= 10;
            }
            if (countDigits%2 == 0){
                count++;
            }
        }
        return count;
    }
}
