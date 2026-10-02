class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        avail = Counter(letters)
        word_counts = [Counter(w) for w in words]
        n = len(words)
        max_total_score = 0
        
        for mask in range(1 << n):
            subset_count = Counter()
            subset_score = 0
            valid = True
            
            for i in range(n):
                if (mask >> i) & 1:
                    wc = word_counts[i]
                    for ch, cnt in wc.items():
                        subset_count[ch] += cnt
                        if subset_count[ch] > avail[ch]:
                            valid = False
                            break
                    if not valid:
                        break
                    subset_score += sum(score[ord(ch) - ord('a')] * cnt for ch, cnt in wc.items())
                    
            if valid:
                max_total_score = max(max_total_score, subset_score)
                
        return max_total_score
