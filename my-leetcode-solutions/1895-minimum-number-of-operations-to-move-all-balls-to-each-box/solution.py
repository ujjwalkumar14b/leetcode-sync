class Solution:
  def minOperations(self, boxes: str) -> list[int]:
    n = len(boxes)
    ans = [0] * n

    # Pass 1: Accumulate operations needed for balls to the left
    balls = 0
    ops = 0
    for i in range(n):
      ans[i] += ops
      balls += int(boxes[i])
      ops += balls

    # Pass 2: Accumulate operations needed for balls to the right
    balls = 0
    ops = 0
    for i in range(n - 1, -1, -1):
      ans[i] += ops
      balls += int(boxes[i])
      ops += balls

    return ans
