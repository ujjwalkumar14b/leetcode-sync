class Solution:
    def replaceDigits(self, s: str) -> str:
        s_list = list(s)        
        for i in range(1, len(s), 2):
            s_list[i] = chr(ord(s_list[i - 1]) + int(s_list[i]))
            
        return "".join(s_list)   
