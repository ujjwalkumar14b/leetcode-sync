class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:

        bitwiseOR = 0
        for num in nums:
            if num % 2 == 0:
                bitwiseOR |= num

        return bitwiseOR
        
