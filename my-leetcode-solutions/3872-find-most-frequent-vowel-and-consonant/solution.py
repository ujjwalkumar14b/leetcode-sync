class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        vowel = 0
        consonant = 0

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if ch in "aeiou":
                vowel = max(vowel, freq[ch])
            else:
                consonant = max(consonant, freq[ch])

        return vowel + consonant
        
