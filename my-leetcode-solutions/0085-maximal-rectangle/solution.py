class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        height = [0] * n
        max_area = 0
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height_idx = stack.pop()
                    height_val = heights[height_idx]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height_val * width)
                stack.append(i)
            
            return max_area
        
        for row in matrix:
            for j in range(n):
                if row[j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            
            max_area = max(max_area, largestRectangleArea(height))
        
        return max_area

