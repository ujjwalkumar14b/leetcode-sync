class Solution {
    public boolean hasSameDigits(String s) {
        char[] t = s.toCharArray();
        int n = t.length;
        
        for (int k = n - 1; k > 1; --k) {
            for (int i = 0; i < k; ++i) {
                int sumModTen = (t[i] - '0' + t[i + 1] - '0') % 10;
                t[i] = (char) (sumModTen + '0');
            }
        }        
        return t[0] == t[1];
    }
}

