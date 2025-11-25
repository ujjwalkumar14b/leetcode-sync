class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        while num >= 10:
            rem = 0
            while num > 0:
                rem += num % 10
                num //= 10
            num = rem
        
        return num

