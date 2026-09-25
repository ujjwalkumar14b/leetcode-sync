class Solution {
    public boolean checkRecord(String s) {
        int absentCount = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            
            if (current == 'A') {
                absentCount++;
                if (absentCount >= 2) {
                    return false;
                }
            }            
            if (current == 'L' 
                && i >= 2 
                && s.charAt(i - 1) == 'L' 
                && s.charAt(i - 2) == 'L') {
                return false;
            }
        }
        return true;
    }
}

