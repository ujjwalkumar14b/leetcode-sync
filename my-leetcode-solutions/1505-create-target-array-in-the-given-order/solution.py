class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target
