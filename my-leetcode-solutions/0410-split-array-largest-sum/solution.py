from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(maxSum):
            count = 1
            current = 0
            
            for num in nums:
                if current + num > maxSum:
                    count += 1
                    current = num
                else:
                    current += num
            
            return count <= k
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
