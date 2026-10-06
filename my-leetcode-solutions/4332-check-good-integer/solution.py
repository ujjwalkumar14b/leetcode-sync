class Solution:
    def checkGoodInteger(self, n: int) -> bool:

        digitSum = 0
        squareSum = 0

        while n > 0:
            rem = n % 10
            digitSum += rem
            squareSum += rem*rem
            n = n // 10
        
        condition = squareSum - digitSum

        return condition >= 50
        
