class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)
        squareSum = 0
        for i in range(1, n+1):
            if n % i == 0:
                squareSum += nums[i-1] * nums[i-1]
            
        return squareSum
        
