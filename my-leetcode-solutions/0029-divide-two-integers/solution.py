class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        is_negative = (dividend < 0) ^ (divisor < 0)        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        quotient = 0
        
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            abs_dividend -= temp_divisor
            quotient += multiple
            
        return -quotient if is_negative else quotient
