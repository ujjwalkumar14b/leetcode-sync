class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])        
        dp = [set() for _ in range(n)]
        dp[0] = {grid[0][0]}
        
        for i in range(m):
            next_dp = [set() for _ in range(n)]
            for j in range(n):
                current_set = set()
                
                if i > 0:
                    current_set.update(dp[j])
                if j > 0:
                    current_set.update(next_dp[j - 1])
                if i == 0 and j == 0:
                    current_set.add(grid[0][0])
                
                if i > 0 or j > 0:
                    next_dp[j] = {val ^ grid[i][j] for val in current_set}
                else:
                    next_dp[j] = current_set
                    
            dp = next_dp
            
        return min(dp[n - 1])
