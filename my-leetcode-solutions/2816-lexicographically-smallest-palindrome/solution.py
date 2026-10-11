class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:
            if s_list[i] != s_list[j]:
                if s_list[i] < s_list[j]:
                    s_list[j] = s_list[i]
                else:
                    s_list[i] = s_list[j]
            i += 1
            j -= 1
            
        return "".join(s_list)
