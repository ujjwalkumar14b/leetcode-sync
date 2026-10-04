class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        
