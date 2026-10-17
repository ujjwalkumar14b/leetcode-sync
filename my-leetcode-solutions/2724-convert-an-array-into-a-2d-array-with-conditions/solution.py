class Solution:
  def findMatrix(self, nums: list[int]) -> list[list[int]]:
    result = []
    freq = {}

    for num in nums:
      row = freq.get(num, 0)
      if row == len(result):
        result.append([])
      result[row].append(num)
      freq[num] = row + 1

    return result
