class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        
        expected = sorted(heights)
        return sum(1 for h, e in zip(heights, expected) if h != e)
