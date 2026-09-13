class Solution {
    public boolean checkValid(int[][] matrix) {
        int n = matrix.length;
        boolean[][] rows = new boolean[n][n];
        boolean[][] cols = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                int val = matrix[i][j] - 1;                
                if (rows[i][val] || cols[j][val]) {
                    return false;
                }                
                rows[i][val] = true;
                cols[j][val] = true;
            }
        }
        return true;
    }
}

