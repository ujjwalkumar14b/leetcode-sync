class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: list[str] | str, queries: list[str]) -> list[bool | None]:
        if isinstance(s, str):
            s = list(s)
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 17
        depth = [0] * n
        parent = [[-1] * LOG for _ in range(n)]
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        def dfs1(u, p, d):
            depth[u] = d
            parent[u][0] = p
            size = 1
            max_subtree = 0
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_subtree:
                        max_subtree = sub_size
                        heavy[u] = v
            return size

        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u][0] and v != heavy[u]:
                    dfs2(v, v)

        dfs1(0, -1, 0)
        for j in range(1, LOG):
            for i in range(n):
                if parent[i][j - 1] != -1:
                    parent[i][j] = parent[parent[i][j - 1]][j - 1]
                    
        dfs2(0, 0)
        
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                pass
            
        inv_pos = [0] * n
        for i in range(n):
            inv_pos[pos[i]] = i
            
        def update_tree(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update_tree(2 * node, start, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

        def query_tree(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            return query_tree(2 * node, start, mid, l, r) ^ query_tree(2 * node + 1, mid + 1, end, l, r)

        for i in range(n):
            c_val = 1 << (ord(s[i]) - ord('a'))
            update_tree(1, 0, n - 1, pos[i], c_val)

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = parent[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_tree(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]][0]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                s[u] = c
                c_val = 1 << (ord(c) - ord('a'))
                update_tree(1, 0, n - 1, pos[u], c_val)
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)

                if (mask & (mask - 1)) == 0:
                    ans.append(True if mask != 0 else True) 
                else:
                    ans.append(False)
        return ans
