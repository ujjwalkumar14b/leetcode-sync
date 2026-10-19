class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1  
        
        score = m * (1 << (n - 1))  
        
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            max_ones = max(ones, m - ones)
            score += max_ones * (1 << (n - 1 - j))
            
        return score
