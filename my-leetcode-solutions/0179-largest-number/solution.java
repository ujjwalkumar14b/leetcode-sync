class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
            return "";
        }
        // Convert int array to String array, so we can sort later on
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]);
        }
        // Comparator to decide which string should come first in concatenation
        Arrays.sort(strs, (str1, str2) -> (str2 + str1).compareTo(str1 + str2));
        // An extreme edge case that you have only a bunch of 0 in your int array
        if (strs[0].charAt(0) == '0') {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s);
        }
        return sb.toString();
    }
}
