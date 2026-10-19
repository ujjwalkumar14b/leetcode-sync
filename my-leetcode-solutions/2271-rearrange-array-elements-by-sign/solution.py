class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        result = []

        for num1, num2 in zip(positive, negative):
            result.append(num1)
            result.append(num2)
        
        return result
      
