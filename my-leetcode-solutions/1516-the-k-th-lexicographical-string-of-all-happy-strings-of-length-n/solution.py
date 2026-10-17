class Solution:
  def getHappyString(self, n: int, k: int) -> str:

    total_strings = 3 * (2 ** (n - 1))
    result = []
    letters = ["a", "b", "c"]
    block_size = 2 ** (n - 1)

    if k > total_strings:
      return ""

    for ch in letters:
      if k <= block_size:
        result.append(ch)
        break
      k -= block_size

    for i in range(1, n):
      block_size = 2 ** (n - 1 - i)
      for ch in letters:
        if ch == result[-1]:
          continue
        if k <= block_size:
          result.append(ch)
          break
        k -= block_size

    return "".join(result)
