class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                new_value = nums[i - 1] + 1
                operations += new_value - nums[i]
                nums[i] = new_value

        return operations
        
