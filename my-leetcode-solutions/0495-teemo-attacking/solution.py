class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
            
        total_time = 0
        for i in range(len(timeSeries) - 1):
            total_time += min(timeSeries[i+1] - timeSeries[i], duration)
            
        total_time += duration
        
        return total_time
