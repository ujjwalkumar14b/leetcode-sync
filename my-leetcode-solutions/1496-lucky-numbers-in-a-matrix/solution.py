class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row_min = [min(row) for row in matrix]
        
        col_max = [
            max(matrix[i][j] for i in range(len(matrix)))
            for j in range(len(matrix[0]))
        ]
        
        return [x for x in row_min if x in col_max]
