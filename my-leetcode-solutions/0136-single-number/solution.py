class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single
