class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:

        even = [num for num in nums if num%2 == 0]
        odd = [num for num in nums if num%2 != 0]
        return even + odd
        
