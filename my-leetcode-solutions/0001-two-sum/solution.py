from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        n = len(nums)
        for left in range(n):
            for right in range(left+ 1, n):
                if(nums[left] + nums[right] == target):
                    return [left, right]
        
        return [-1, -1]
