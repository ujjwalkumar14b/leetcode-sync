class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int provinceCount = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                // Start a new DFS for each unvisited city
                dfs(isConnected, visited, i);
                provinceCount++;
            }
        }
        
        return provinceCount;
    }
    
    private void dfs(int[][] isConnected, boolean[] visited, int city) {
        visited[city] = true; // Mark the city as visited
        
        for (int i = 0; i < isConnected.length; i++) {
            // If the city is connected and not yet visited
            if (isConnected[city][i] == 1 && !visited[i]) {
                dfs(isConnected, visited, i); // Visit the connected city
            }
        }
    }
}

