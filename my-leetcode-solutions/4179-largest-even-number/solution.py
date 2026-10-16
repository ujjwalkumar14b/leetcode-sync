class Solution:
    def largestEven(self, s: str) -> str:
        last_two_idx = s.rfind('2')
        
        if last_two_idx == -1:
            return ""
            
        return s[:last_two_idx + 1]
