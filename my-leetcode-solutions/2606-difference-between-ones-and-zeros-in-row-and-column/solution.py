class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        
        onesRow = [sum(row) for row in grid]
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        zerosRow = [m - val for val in onesRow]
        zerosCol = [n - val for val in onesCol]
        
        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                
        return diff
