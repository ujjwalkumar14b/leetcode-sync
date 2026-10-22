class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]

        return transposed
        
