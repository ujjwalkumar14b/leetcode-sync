class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0

        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        
        return count 
        
