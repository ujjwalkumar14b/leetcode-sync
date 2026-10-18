class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            if num % 2 == 0 and count == 1:
                return num
                break 
        
        return -1
        
