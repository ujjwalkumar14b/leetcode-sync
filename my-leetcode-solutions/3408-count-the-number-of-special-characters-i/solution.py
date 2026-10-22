class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        count = 0
        
        for c in set(word.lower()):
            if c in chars and c.upper() in chars:
                count += 1
                
        return count
