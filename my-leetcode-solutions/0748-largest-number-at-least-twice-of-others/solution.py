class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = -1
        second_largest = -1
        largest_idx = -1
        
        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                largest_idx = i
            elif num > second_largest:
                second_largest = num
                
        if largest >= 2 * second_largest:
            return largest_idx
        else:
            return -1
