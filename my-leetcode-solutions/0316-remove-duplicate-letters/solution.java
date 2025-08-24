import java.util.*;
class Solution {
    public String removeDuplicateLetters(String s) {
        int[] freq = new int[26];
        boolean[] inStack = new boolean[26];
        
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            freq[c - 'a']--;

            if (inStack[c - 'a']) continue;

            while (!stack.isEmpty() && stack.peek() > c && freq[stack.peek() - 'a'] > 0) {
                inStack[stack.pop() - 'a'] = false;
            }

            stack.push(c);
            inStack[c - 'a'] = true;
        }

        StringBuilder result = new StringBuilder();
        for (char c : stack) result.append(c);

        return result.toString();
    }
}
