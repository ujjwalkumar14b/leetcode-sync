class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for digit in range(len(s)-1):
            if abs(int(s[digit]) - int(s[digit+1])) > 2:
                return False
                break

        return True
        
