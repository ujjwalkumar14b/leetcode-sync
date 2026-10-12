class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        max_nums = [0] * k
        total_sum = 0
        
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        for i in range(31):
            for j in range(min(bit_counts[i], k)):
                max_nums[j] |= (1 << i)
                
        for num in max_nums:
            total_sum = (total_sum + num * num) % MOD
            
        return total_sum
