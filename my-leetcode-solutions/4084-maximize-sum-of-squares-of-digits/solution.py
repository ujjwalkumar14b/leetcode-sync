class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9 * num:
            return ""
            
        result = []
        remaining_sum = sum
        remaining_digits = num
        
        while remaining_digits > 0:
            digit = min(9, remaining_sum)
            
            while digit >= 0:
                if remaining_sum - digit <= 9 * (remaining_digits - 1):
                    break
                digit -= 1
                
            result.append(str(digit))
            remaining_sum -= digit
            remaining_digits -= 1
            
        return "".join(result)
