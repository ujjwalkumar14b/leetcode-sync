import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");    
        Map<Character, String> charToWord = new HashMap<>();
        Map<String, Character> wordToChar = new HashMap<>();    
        
        if (pattern.length() != words.length) {
            return false;
        }
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];
            
            if (charToWord.containsKey(c) && !charToWord.get(c).equals(word)) {
                return false;
            }            
            if (wordToChar.containsKey(word) && wordToChar.get(word) != c) {
                return false;
            }            
            charToWord.put(c, word);
            wordToChar.put(word, c);
        }
        return true;
    }
}

