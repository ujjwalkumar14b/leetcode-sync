class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            for digit in str(num):
                ans.append(int(digit))

        return ans
        
