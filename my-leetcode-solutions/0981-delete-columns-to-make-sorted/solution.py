class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        delete_count = 0

        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break 

        return delete_count
        
