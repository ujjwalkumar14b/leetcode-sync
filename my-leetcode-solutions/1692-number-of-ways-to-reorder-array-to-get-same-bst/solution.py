import math
from functools import cache

class Solution:
  def numOfWays(self, nums: list[int]) -> int:
    MOD = 10**9 + 7

    @cache
    def dfs(sub_nums):
      if len(sub_nums) <= 2:
        return 1

      root = sub_nums[0]
      left = [x for x in sub_nums if x < root]
      right = [x for x in sub_nums if x > root]

      ways_left = dfs(tuple(left))
      ways_right = dfs(tuple(right))

      return (
          math.comb(len(left) + len(right), len(left))
          * ways_left
          * ways_right
      ) % MOD

    return (dfs(tuple(nums)) - 1) % MOD
