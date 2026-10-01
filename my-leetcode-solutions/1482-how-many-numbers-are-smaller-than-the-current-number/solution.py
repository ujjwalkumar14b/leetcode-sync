class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        sorted_nums = sorted(nums)
        first_index = {}
        
        for idx, num in enumerate(sorted_nums):
            if num not in first_index:
                first_index[num] = idx
                
        return [first_index[num] for num in nums]
