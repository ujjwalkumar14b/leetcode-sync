class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        
        while len(word) < k:
            next_part = []
            for char in word:
                next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                next_part.append(next_char)
            word.extend(next_part)
            
        return word[k - 1]
