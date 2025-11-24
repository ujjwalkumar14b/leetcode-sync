class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # negative numbers are not palindromes
        if x < 0:
            return False
        
        num = x
        reversed_num = 0
        
        while num > 0:
            rem = num % 10
            reversed_num = reversed_num * 10 + rem
            num //= 10
        
        return reversed_num == x

