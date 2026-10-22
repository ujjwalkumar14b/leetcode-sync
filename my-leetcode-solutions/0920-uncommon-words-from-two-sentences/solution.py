class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
    words = s1.split() + s2.split()
    word_count = {}
    
    for word in words:
      word_count[word] = word_count.get(word, 0) + 1

    return [word for word, count in word_count.items() if count == 1]
