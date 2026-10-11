class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        num = x
        digitSum = 0
        while num > 0:
            rem = num % 10
            digitSum += rem
            num = num // 10
        
        if x % digitSum == 0:
            return digitSum
        
        return -1
        
