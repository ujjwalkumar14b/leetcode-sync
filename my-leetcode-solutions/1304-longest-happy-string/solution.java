class Solution {
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder result = new StringBuilder();

        while (a > 0 || b > 0 || c > 0) {
            // Get the counts and characters as a 2D array
            char[] chars = new char[3];
            int[] counts = new int[3];
            
            // Fill the arrays with characters and their respective counts
            if (a > 0) {
                chars[0] = 'a';
                counts[0] = a;
            }
            if (b > 0) {
                chars[1] = 'b';
                counts[1] = b;
            }
            if (c > 0) {
                chars[2] = 'c';
                counts[2] = c;
            }
            
            // Find the character with the maximum count
            int maxIndex = -1;
            for (int i = 0; i < 3; i++) {
                if (maxIndex == -1 || counts[i] > counts[maxIndex]) {
                    maxIndex = i;
                }
            }
            
            // If the last two characters are the same, we cannot use the max character
            if (result.length() >= 2 && result.charAt(result.length() - 1) == chars[maxIndex] && 
                result.charAt(result.length() - 2) == chars[maxIndex]) {
                // We need to find the next character with a positive count
                int secondMaxIndex = -1;
                for (int i = 0; i < 3; i++) {
                    if (i != maxIndex && counts[i] > 0) {
                        secondMaxIndex = i;
                        break;
                    }
                }
                
                // If we can't find a second character to append, we break
                if (secondMaxIndex == -1) {
                    break;
                }
                
                // Append the second character
                result.append(chars[secondMaxIndex]);
                // Decrement the count
                if (secondMaxIndex == 0) a--;
                else if (secondMaxIndex == 1) b--;
                else c--;
            } else {
                // Append the character with the maximum count
                result.append(chars[maxIndex]);
                // Decrement the count
                if (maxIndex == 0) a--;
                else if (maxIndex == 1) b--;
                else c--;
            }
        }

        return result.toString();
    }
}

