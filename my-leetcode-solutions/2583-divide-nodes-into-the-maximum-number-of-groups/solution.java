import java.util.*;

class Solution {

    // UnionFind class as a static inner class
    static class UnionFind {
        private int[] id;
        private int[] rank;

        public UnionFind(int n) {
            id = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                id[i] = i;
            }
        }

        public void unionByRank(int u, int v) {
            int i = find(u);
            int j = find(v);
            if (i == j) return;
            if (rank[i] < rank[j]) {
                id[i] = j;
            } else if (rank[i] > rank[j]) {
                id[j] = i;
            } else {
                id[i] = j;
                rank[j]++;
            }
        }

        public int find(int u) {
            if (id[u] != u) {
                id[u] = find(id[u]); // Path compression
            }
            return id[u];
        }
    }

    public int magnificentSets(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        UnionFind uf = new UnionFind(n);
        Map<Integer, Integer> rootToGroupSize = new HashMap<>();

        // Build the graph and apply union-find
        for (int[] edge : edges) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph.get(u).add(v);
            graph.get(v).add(u);
            uf.unionByRank(u, v);
        }

        // Process each node
        for (int i = 0; i < n; i++) {
            int newGroupSize = bfs(graph, i);
            if (newGroupSize == -1) {
                return -1; // If a cycle is detected, return -1
            }
            int root = uf.find(i);
            rootToGroupSize.put(root, Math.max(rootToGroupSize.getOrDefault(root, 0), newGroupSize));
        }

        // Calculate the result
        int ans = 0;
        for (int groupSize : rootToGroupSize.values()) {
            ans += groupSize;
        }

        return ans;
    }

    private int bfs(List<List<Integer>> graph, int u) {
        int step = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(u);
        Map<Integer, Integer> nodeToStep = new HashMap<>();
        nodeToStep.put(u, 1);

        while (!q.isEmpty()) {
            step++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int node = q.poll();
                for (int neighbor : graph.get(node)) {
                    if (!nodeToStep.containsKey(neighbor)) {
                        q.add(neighbor);
                        nodeToStep.put(neighbor, step + 1);
                    } else if (nodeToStep.get(neighbor) == step) {
                        // If there's an odd cycle, return -1
                        return -1;
                    }
                }
            }
        }

        return step;
    }
}

