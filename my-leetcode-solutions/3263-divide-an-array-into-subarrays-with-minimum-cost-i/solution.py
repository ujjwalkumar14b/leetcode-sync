class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]        
        rest_sorted = sorted(nums[1:])        
        return first + rest_sorted[0] + rest_sorted[1]
        
