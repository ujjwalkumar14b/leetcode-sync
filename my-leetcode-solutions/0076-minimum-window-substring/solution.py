class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        from collections import Counter
        
        t_count = Counter(t)
        window_count = {}
        have = 0
        need = len(t_count)
        
        res = [-1, -1]
        res_len = float("inf")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

