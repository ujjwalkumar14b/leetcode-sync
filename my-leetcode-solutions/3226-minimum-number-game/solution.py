class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        arr = []
        while len(nums) != 0:
            a_num = min(nums)
            nums.remove(a_num)
            b_num = min(nums)
            nums.remove(b_num)

            arr.append(b_num)
            arr.append(a_num)
        
        return arr
        
