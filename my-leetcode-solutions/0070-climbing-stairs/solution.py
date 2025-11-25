class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        
        def solve(x):
            if x in memo:
                return memo[x]
            memo[x] = solve(x-1) + solve(x-2)
            return memo[x]
        
        return solve(n)

