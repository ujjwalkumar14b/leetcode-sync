class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 10:
                if nums[i] == i:
                    return i
                    break
            else:
                n = nums[i]
                digitSum = 0
                while n > 0:
                    rem = n % 10
                    digitSum += rem
                    n = n // 10
                
                if digitSum == i:
                    return i
                    break
        
        return -1
        
