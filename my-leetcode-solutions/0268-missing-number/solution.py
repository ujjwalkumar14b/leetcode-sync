class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(nums)

        for i in range(n + 1):
            if i not in num_set:
                return i

