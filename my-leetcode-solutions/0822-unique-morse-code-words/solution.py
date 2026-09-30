class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        
        transformations = set()
        for word in words:
            code = "".join(morse_code[ord(char) - ord('a')] for char in word)
            transformations.add(code)
            
        return len(transformations)
