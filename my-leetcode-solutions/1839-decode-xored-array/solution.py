class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        res = [first]
        for val in encoded:
            res.append(res[-1] ^ val)
        return res
