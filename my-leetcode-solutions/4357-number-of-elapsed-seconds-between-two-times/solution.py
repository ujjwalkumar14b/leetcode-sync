class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        
        def to_seconds(t: str) -> int:
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s

        return to_seconds(endTime) - to_seconds(startTime)
