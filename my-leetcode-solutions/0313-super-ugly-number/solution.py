class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        dp = [1] * n        
        k = len(primes)
        pointers = [0] * k
        
        for i in range(1, n):
            next_ugly = min(dp[pointers[j]] * primes[j] for j in range(k))            
            dp[i] = next_ugly
            
            for j in range(k):
                if dp[pointers[j]] * primes[j] == next_ugly:
                    pointers[j] += 1
                    
        return dp[-1]
