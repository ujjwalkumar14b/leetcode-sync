class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:

        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            if count > 0.25 * len(arr):
                return num

