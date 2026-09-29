class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x > 0:
            sign = 1
        else:
            sign = -1

        num = x
        reverse = 0
        while num > 0:
            rem = num % 10
            reverse = reverse * 10 + rem
            num = num // 10
        
        palindrome = sign * reverse

        if x == palindrome:
            return True
        else:
            return False
        

