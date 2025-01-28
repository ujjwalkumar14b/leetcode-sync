class Solution {
  
    private int[][] grid; 
    private int rows; 
    private int cols; 
    public int findMaxFish(int[][] grid) {
        rows = grid.length; 
        cols = grid[0].length; 
        this.grid = grid; 
        int maxFishCount = 0; 
      
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] > 0) {
                    maxFishCount = Math.max(maxFishCount, dfs(i, j));
                }
            }
        }
        return maxFishCount;
    }

    private int dfs(int i, int j) {
        int fishCount = grid[i][j]; 
        grid[i][j] = 0; 
        int[] directions = {-1, 0, 1, 0, -1};
      
        for (int k = 0; k < 4; ++k) {
            int x = i + directions[k]; 
            int y = j + directions[k + 1]; 
          
            if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] > 0) {
                fishCount += dfs(x, y); 
            }
        }
        return fishCount;
    }
}

