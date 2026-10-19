class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result
        
