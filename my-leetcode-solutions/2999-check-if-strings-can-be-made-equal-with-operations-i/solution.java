class Solution {
    public boolean canBeEqual(String s1, String s2) {
        return check(s1, s2, 0) && check(s1, s2, 1);
    }
    private boolean check(String s1, String s2, int start) {
        char a = s1.charAt(start);
        char b = s1.charAt(start + 2);
        char c = s2.charAt(start);
        char d = s2.charAt(start + 2);
        
        return (a == c && b == d) || (a == d && b == c);
    }
}

