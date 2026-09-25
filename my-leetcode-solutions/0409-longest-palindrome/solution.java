import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> charCount = new HashMap<>();
        int palindromeLength = 0;
        boolean hasOdd = false;
        
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }        
        for (int count : charCount.values()) {
            palindromeLength += (count / 2) * 2;
            if (count % 2 == 1) {
                hasOdd = true;
            }
        }        
        if (hasOdd) {
            palindromeLength += 1;
        }
        return palindromeLength;
    }
}

