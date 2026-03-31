from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        # If the starting pixel already has the target color, no work needed
        if start_color == color:
            return image

        def dfs(r, c):
            # boundary + color check
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != start_color:
                return
            
            # recolor
            image[r][c] = color

            # explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
