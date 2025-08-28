class Solution {
    public String reverseWords(String s) {
        // Step 1: trim leading/trailing spaces, then split by whitespace
        String[] words = s.trim().split("\\s+");

        // Step 2: reverse the words
        StringBuilder result = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]);
            if (i > 0) result.append(" ");
        }

        return result.toString();
    }
}

