class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        minSum = float('inf')
        for arr in tasks:
            minSum = min(minSum, sum(arr))
        
        return minSum
            
