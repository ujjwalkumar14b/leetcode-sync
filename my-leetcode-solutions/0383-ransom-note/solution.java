class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] letterCounts = new int[26];
        
        for (int i = 0; i < magazine.length(); i++) {
            letterCounts[magazine.charAt(i) - 'a']++;
        }        
        for (int i = 0; i < ransomNote.length(); i++) {
            int index = ransomNote.charAt(i) - 'a';
            letterCounts[index]--;
            
            if (letterCounts[index] < 0) {
                return false;
            }
        }
        return true;
    }
}

