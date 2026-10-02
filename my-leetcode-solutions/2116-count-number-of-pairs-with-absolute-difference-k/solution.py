class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        freq = {}
        count = 0

        for x in nums:
            count += freq.get(x - k, 0)
            count += freq.get(x + k, 0)

            freq[x] = freq.get(x, 0) + 1

        return count

