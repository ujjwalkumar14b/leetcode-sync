class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                num = int(s[i:i + 2])
                res.append(chr(ord('a') + num - 1))
                i += 3
            else:
                num = int(s[i])
                res.append(chr(ord('a') + num - 1))
                i += 1
                
        return "".join(res)
