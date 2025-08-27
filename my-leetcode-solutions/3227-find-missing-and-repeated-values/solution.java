import java.util.*;

class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int[] count = new int[n * n + 1]; // To count occurrences from 1 to n^2

        // Count each number in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count[grid[i][j]]++;
            }
        }

        int duplicate = -1;
        int missing = -1;

        // Find the duplicate and missing numbers
        for (int i = 1; i <= n * n; i++) {
            if (count[i] == 2) {
                duplicate = i;
            } else if (count[i] == 0) {
                missing = i;
            }
        }

        return new int[]{duplicate, missing};
    }
}

