class Solution {
    public int projectionArea(int[][] grid) {
        
        int n = grid.length;
        int top = 0;   // xy-plane projection
        int front = 0; // yz-plane projection
        int side = 0;  // zx-plane projection

        for (int i = 0; i < n; i++) {
            int rowMax = 0;
            int colMax = 0;
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    top++;
                }
                rowMax = Math.max(rowMax, grid[i][j]);
                colMax = Math.max(colMax, grid[j][i]);
            }
            front += rowMax;
            side += colMax;
        }
        return top + front + side;
    }
}
