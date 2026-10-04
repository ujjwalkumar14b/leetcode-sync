class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        total = 0

        for x in nums:
            if nums.count(x) == 1:
                total += x

        return total
        
