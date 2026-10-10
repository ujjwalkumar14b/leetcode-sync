class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        for i in range(32):
            ones = 0
            mask = 1 << i
            
            for num in nums:
                if num & mask:
                    ones += 1
                    
            zeros = n - ones            
            total_distance += zeros * ones
            
        return total_distance
