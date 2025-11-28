class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:

            # traverse left → right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # traverse top → bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # traverse right → left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # traverse bottom → top
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result

