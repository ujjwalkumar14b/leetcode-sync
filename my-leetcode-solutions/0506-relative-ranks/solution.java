import java.util.Arrays;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        String[] ans = new String[n];        
        Integer[] indices = new Integer[n];

        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        
        Arrays.sort(indices, (a, b) -> Integer.compare(score[b], score[a]));
        
        for (int i = 0; i < n; i++) {
            int originalIndex = indices[i];
            if (i == 0) {
                ans[originalIndex] = "Gold Medal";
            } else if (i == 1) {
                ans[originalIndex] = "Silver Medal";
            } else if (i == 2) {
                ans[originalIndex] = "Bronze Medal";
            } else {
                ans[originalIndex] = String.valueOf(i + 1);
            }
        }
        return ans;
    }
}

