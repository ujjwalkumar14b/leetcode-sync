class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        return [[1 - pixel for pixel in row[::-1]] for row in image]
