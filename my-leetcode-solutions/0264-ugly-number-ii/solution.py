class Solution:

  def nthUglyNumber(self, n: int) -> int:
    dp = [0] * n
    dp[0] = 1

    i2 = i3 = i5 = 0

    for i in range(1, n):
      next_2 = dp[i2] * 2
      next_3 = dp[i3] * 3
      next_5 = dp[i5] * 5

      next_ugly = min(next_2, next_3, next_5)
      dp[i] = next_ugly

      if next_ugly == next_2:
        i2 += 1
      if next_ugly == next_3:
        i3 += 1
      if next_ugly == next_5:
        i5 += 1

    return dp[-1]
