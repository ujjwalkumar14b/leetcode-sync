class Solution {
    public int maximumSwap(int num) {
        // Convert the number to a character array of digits
        char[] digits = Integer.toString(num).toCharArray();
        
        // Create an array to store the last occurrence of each digit (0-9)
        int[] last = new int[10];
        for (int i = 0; i < digits.length; i++) {
            last[digits[i] - '0'] = i; // Store the last occurrence of each digit
        }
        
        // Iterate through the digits to find the first place to swap
        for (int i = 0; i < digits.length; i++) {
            // Check for digits larger than digits[i] from 9 to digits[i] + 1
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (last[d] > i) { // If a larger digit exists later
                    // Swap the digits
                    char temp = digits[i];
                    digits[i] = digits[last[d]];
                    digits[last[d]] = temp;
                    
                    // Return the result as an integer
                    return Integer.parseInt(new String(digits));
                }
            }
        }
        
        return num; // If no swap is made, return the original number
    }
}

