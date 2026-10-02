class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for n = 1
        aba = 6  # 2-color row patterns
        abc = 6  # 3-color row patterns
        
        for _ in range(n - 1):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD
