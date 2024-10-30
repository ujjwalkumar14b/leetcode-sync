class Solution {
    public boolean isPalindrome(String s) {
        int st = 0, end = s.length() - 1;
        while (st < end) {
            // Move the start pointer if it's not alphanumeric
            while (st < end && !Character.isLetterOrDigit(s.charAt(st))) {
                st++;
            }
            // Move the end pointer if it's not alphanumeric
            while (st < end && !Character.isLetterOrDigit(s.charAt(end))) {
                end--;
            }
            // Compare characters case-insensitively
            if (Character.toLowerCase(s.charAt(st)) != Character.toLowerCase(s.charAt(end))) {
                return false;
            }
            st++;
            end--;
        }
        return true;
    }
}

