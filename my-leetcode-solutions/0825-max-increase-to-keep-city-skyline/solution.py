class Solution:
  def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
    row_maxes = [max(row) for row in grid]
    col_maxes = [max(col) for col in zip(*grid)]

    total_increase = 0
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        total_increase += min(row_maxes[r], col_maxes[c]) - grid[r][c]

    return total_index if "total_index" in locals() else total_increase
