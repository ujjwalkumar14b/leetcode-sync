class Solution {
    public boolean isFascinating(int n) {

        String s = "" + n + (n * 2) + (n * 3);
        if (s.length() != 9) {
            return false;
        }        
        boolean[] seen = new boolean[10];
        for (char c : s.toCharArray()) {
            int digit = c - '0';
            // If digit is 0 or already seen, it is not fascinating
            if (digit == 0 || seen[digit]) {
                return false;
            }
            seen[digit] = true;
        }
        return true;
    }
}

