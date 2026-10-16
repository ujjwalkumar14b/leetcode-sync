class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sum_sq = [0] * (4 * n)
        sum_c = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, length, val):
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_c[node] + val * val * length) % MOD
            sum_c[node] = (sum_c[node] + val * length) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, L, R):
            if lazy[node] != 0:
                mid = (L + R) // 2
                apply(2 * node, mid - L + 1, lazy[node])
                apply(2 * node + 1, R - mid, lazy[node])
                lazy[node] = 0

        def update(node, L, R, ql, qr, val):
            if ql <= L and R <= qr:
                apply(node, R - L + 1, val)
                return
                
            push(node, L, R)
            mid = (L + R) // 2
            
            if ql <= mid:
                update(2 * node, L, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, R, ql, qr, val)
                
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            sum_c[node] = (sum_c[2 * node] + sum_c[2 * node + 1]) % MOD

        total_ans = 0
        last_seen = {}
        
        for i, x in enumerate(nums):
            start_idx = last_seen.get(x, -1) + 1            
            update(1, 0, n - 1, start_idx, i, 1)            
            total_ans = (total_ans + sum_sq[1]) % MOD            
            last_seen[x] = i
            
        return total_ans
