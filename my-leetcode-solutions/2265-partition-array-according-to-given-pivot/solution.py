class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        
        return less + equal + greater
     
