class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digit_sum = 0
        
        while n > 0:
            digit_sum += n % k
            n //= k
            
        return digit_sum    
