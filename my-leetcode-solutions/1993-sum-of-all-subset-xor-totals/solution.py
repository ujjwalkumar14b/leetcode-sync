class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        bitwise_or = 0
        for num in nums:
            bitwise_or |= num
            
        return bitwise_or * (1 << (len(nums) - 1))
 
