class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        min_so_far = float("inf")

        for c in cost:
            min_so_far = min(min_so_far, c)
            ans.append(min_so_far)

        return ans
