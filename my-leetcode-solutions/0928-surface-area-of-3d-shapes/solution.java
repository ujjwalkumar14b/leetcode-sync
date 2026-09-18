class Solution {
    public int surfaceArea(int[][] grid) {
        
        int totalArea = 0;
        int n = grid.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int height = grid[i][j];
                
                if (height > 0) {
                    totalArea += (height * 4) + 2;

                    if (i > 0) {
                        totalArea -= Math.min(height, grid[i - 1][j]) * 2;
                    }
                    if (j > 0) {
                        totalArea -= Math.min(height, grid[i][j - 1]) * 2;
                    }
                }
            }
        }
        return totalArea;
    }
}
