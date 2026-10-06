class Solution:
    def minMoves(self, nums: List[int]) -> int:

        moves = 0
        maxNum = max(nums)

        for num in nums:
            rem = maxNum - num
            moves += rem
        
        return moves
        
