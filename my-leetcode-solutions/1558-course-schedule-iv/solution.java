class Solution {

    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        boolean[][] transitiveClosure = new boolean[numCourses][numCourses];
        List<Integer>[] graph = new List[numCourses];
        int[] inDegree = new int[numCourses]; 

        Arrays.setAll(graph, i -> new ArrayList<>());
      
        for (int[] prerequisite : prerequisites) {
            graph[prerequisite[0]].add(prerequisite[1]);
            ++inDegree[prerequisite[1]]; 
        }
      
        Deque<Integer> queue = new ArrayDeque<>();
      
        for (int i = 0; i < numCourses; ++i) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }      
        while (!queue.isEmpty()) {
            int course = queue.poll();          
            for (int neighbor : graph[course]) {
              
                transitiveClosure[course][neighbor] = true;              
                for (int preCourse = 0; preCourse < numCourses; ++preCourse) {
                    transitiveClosure[preCourse][neighbor] |= transitiveClosure[preCourse][course];
                }              
                if (--inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        List<Boolean> answers = new ArrayList<>();
      
        for (int[] query : queries) {
            answers.add(transitiveClosure[query[0]][query[1]]);
        }
      
        return answers;
    }
}
