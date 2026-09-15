import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);
        
        int childPointer = 0;
        int cookiePointer = 0;
        
        while (childPointer < g.length && cookiePointer < s.length) {
            if (s[cookiePointer] >= g[childPointer]) {
                childPointer++;
            }
            cookiePointer++;
        }        
        return childPointer;
    }
}

