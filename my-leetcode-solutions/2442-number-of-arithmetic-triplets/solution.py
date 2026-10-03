class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        seen = set(nums)
        count = 0

        for num in nums:
            if num + diff in seen and num + 2 * diff in seen:
                count += 1

        return count
        
