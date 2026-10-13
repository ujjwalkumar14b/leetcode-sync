class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        sq = sorted(x * x for x in nums)
        half = len(sq) // 2
        return sum(sq) - 2 * sum(sq[:half])
        
