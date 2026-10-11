class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        sumElement = 0
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                sumElement += nums[i]

        return sumElement
        
