class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elementSum = sum(num for num in nums)
        digitSum = sum(int(digit) for num in nums for digit in str(num))
        return abs(elementSum - digitSum)
       
