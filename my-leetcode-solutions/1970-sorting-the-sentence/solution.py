class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)
        
        for word in words:
            position = int(word[-1]) - 1
            actual_word = word[:-1]
            res[position] = actual_word
            
        return " ".join(res)
