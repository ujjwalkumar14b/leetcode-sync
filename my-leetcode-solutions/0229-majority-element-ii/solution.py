class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        for num, count in freq.items():
            if count > len(nums) // 3:
                ans.append(num)

        return ans
