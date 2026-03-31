from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0 and 1 are two colors

        for i in range(n):
            if color[i] != -1:
                continue

            # start BFS
            queue = deque([i])
            color[i] = 0

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
