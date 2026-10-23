class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        ans = None
        for i, num in enumerate(nums):
            if num != i:
                if ans is None:
                    ans = num
                else:
                    ans &= num
                    
        return ans if ans is not None else 0
        
