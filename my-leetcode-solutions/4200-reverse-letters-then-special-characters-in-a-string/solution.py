class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        specials = [ch for ch in s if not ch.isalpha()]

        res = []
        for ch in s:
            if ch.isalpha():
                res.append(letters.pop())
            else:
                res.append(specials.pop())

        return "".join(res)
