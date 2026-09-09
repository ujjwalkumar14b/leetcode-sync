class Solution {
    public boolean halvesAreAlike(String s) {
        int n = s.length();
        int mid = n / 2;
        int count = 0;
        String vowels = "aeiouAEIOU";
        
        for (int i = 0; i < mid; i++) {
            char c1 = s.charAt(i);
            char c2 = s.charAt(i + mid);
            
            if (vowels.indexOf(c1) >= 0) {
                count++;
            }
            if (vowels.indexOf(c2) >= 0) {
                count--;
            }
        }
        return count == 0;
    }
}

