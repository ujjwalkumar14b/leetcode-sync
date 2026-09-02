class Solution {
    public String largestGoodInteger(String num) {
        char largest = 0;

        for (int i = 0; i < num.length() - 2; i++) {
            if (num.charAt(i) == num.charAt(i + 1) &&
                num.charAt(i) == num.charAt(i + 2)) {
                
                largest = (char) Math.max(largest, num.charAt(i));
            }
        }
        return largest == 0 ? "" : "" + largest + largest + largest;
    }
}

