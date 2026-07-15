class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_occurrence = {0: -1}
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in first_occurrence:
                max_len = max(max_len, i - first_occurrence[count])
            else:
                first_occurrence[count] = i

        return max_len
