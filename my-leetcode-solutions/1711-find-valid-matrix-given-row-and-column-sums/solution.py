class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        
        m, n = len(rowSum), len(colSum)
        mat = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                mat[i][j] = min(rowSum[i], colSum[j])                
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]
                
        return mat
