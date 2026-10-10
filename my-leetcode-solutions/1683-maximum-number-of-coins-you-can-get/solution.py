class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        n = len(piles)
        ans = 0
        for i in range(n // 3, n, 2):
            ans += piles[i]
            
        return ans
