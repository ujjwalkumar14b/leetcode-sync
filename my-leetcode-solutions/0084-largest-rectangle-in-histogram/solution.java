import java.util.Stack;
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int maxArea = 0;

        // Stack will store indices of bars
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i <= n; i++) {
            // For the last iteration, take height as 0 to flush out stack
            int h = (i == n) ? 0 : heights[i];

            // While current bar is lower than top of stack → pop & calculate area
            while (!stack.isEmpty() && h < heights[stack.peek()]) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }

        return maxArea;
    }
}

