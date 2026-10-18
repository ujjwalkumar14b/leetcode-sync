class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()        
        first_group_len = len(s) % k
        groups = []
        
        if first_group_len > 0:
            groups.append(s[:first_group_len])
            
        for i in range(first_group_len, len(s), k):
            groups.append(s[i:i + k])
            
        return "-".join(groups)
