class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:

        string = ""
        for num in nums:
            string += str(num)

        return string.count(str(digit))

