class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())

        left, right = 0, len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True

