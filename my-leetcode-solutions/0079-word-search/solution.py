class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            board[r][c] = temp
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
