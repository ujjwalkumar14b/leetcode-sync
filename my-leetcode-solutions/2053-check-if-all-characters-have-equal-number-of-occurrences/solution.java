class Solution {
    public boolean areOccurrencesEqual(String s) {
        
        int[] count = new int[26];
        int reference = 0;
        
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }        
        for (int freq : count) {
            if (freq == 0) continue;
            if (reference == 0) {
                reference = freq;
            } else if (reference != freq) {
                return false;
            }
        }
        return true;
    }
}

