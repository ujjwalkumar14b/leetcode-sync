class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0

        for ch in s:
            ans ^= ord(ch)

        for ch in t:
            ans ^= ord(ch)

        return chr(ans)
