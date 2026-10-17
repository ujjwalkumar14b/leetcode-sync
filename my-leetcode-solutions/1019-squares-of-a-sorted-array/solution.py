class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]

        return sorted(nums)
        
