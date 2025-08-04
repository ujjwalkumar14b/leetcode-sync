class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        int result = 0;
        int sign = 1;

        // Skip leading whitespaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        // Handle optional '+' or '-'
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        // Process digits
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // Check for overflow
            if (result > (Integer.MAX_VALUE - digit) / 10) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }
}

