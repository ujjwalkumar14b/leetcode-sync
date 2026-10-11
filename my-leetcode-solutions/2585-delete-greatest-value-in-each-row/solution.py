class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:

        for row in grid:
            row.sort()
            
        total_sum = 0
        m, n = len(grid), len(grid[0])
        
        for j in range(n):
            max_in_col = 0
            for i in range(m):
                max_in_col = max(max_in_col, grid[i][j])
            total_sum += max_in_col
            
        return total_sum
        
