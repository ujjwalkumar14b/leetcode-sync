class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty_count = 0
        start_r = start_c = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != -1:
                    empty_count += 1
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    
        self.paths = 0
        
        def dfs(r: int, c: int, remain: int):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == -1:
                return
            
            if grid[r][c] == 2:
                if remain == 1:
                    self.paths += 1
                return
            
            temp = grid[r][c]
            grid[r][c] = -1
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, remain - 1)
                
            grid[r][c] = temp

        dfs(start_r, start_c, empty_count)
        return self.paths
