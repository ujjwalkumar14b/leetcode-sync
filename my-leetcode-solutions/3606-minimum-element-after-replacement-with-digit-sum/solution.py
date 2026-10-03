class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        result = []
        for num in nums:
            digitSum = 0

            while num > 0:
                rem = num % 10
                digitSum += rem
                num = num // 10
            
            result.append(digitSum)
        
        return min(result)
