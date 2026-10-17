class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = list(range(1, m + 1))
        result = []

        for q in queries:
            idx = p.index(q)
            result.append(idx)
            p.insert(0, p.pop(idx))

        return result
