class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start_idx: int, current_path: List[int], current_sum: int):
            if current_sum == target:
                res.append(list(current_path))
                return

            if current_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                current_path.append(candidates[i])
                backtrack(i, current_path, current_sum + candidates[i])
                current_path.pop()  

        backtrack(0, [], 0)
        return res
