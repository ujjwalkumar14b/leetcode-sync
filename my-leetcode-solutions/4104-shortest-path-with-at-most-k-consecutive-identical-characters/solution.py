from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        pq = [(0, 0, 1)]        
        dist = {}
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return w
                
            if (u, count) in dist and dist[(u, count)] < w:
                continue
                
            for v, weight in graph[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count <= k:
                    next_w = w + weight
                    if (v, next_count) not in dist or next_w < dist[(v, next_count)]:
                        dist[(v, next_count)] = next_w
                        heapq.heappush(pq, (next_w, v, next_count))
                        
        return -1
