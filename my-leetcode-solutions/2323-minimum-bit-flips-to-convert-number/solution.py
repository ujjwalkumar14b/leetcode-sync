class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        xor_result = start ^ goal        
        count = 0
        while xor_result > 0:
            xor_result &= xor_result - 1
            count += 1
            
        return count
        
