class Solution {
    private Integer prev = null;
    private int currentCount = 0;
    private int maxCount = 0;
    private List<Integer> modes = new ArrayList<>();

    public int[] findMode(TreeNode root) {
        inOrder(root);
        
        int[] result = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) {
            result[i] = modes.get(i);
        }
        return result;
    }

    private void inOrder(TreeNode node) {
        if (node == null) return;

        inOrder(node.left);

        if (prev != null && node.val == prev) {
            currentCount++;
        } else {
            currentCount = 1;
        }

        if (currentCount > maxCount) {
            maxCount = currentCount;
            modes.clear(); 
            modes.add(node.val);
        } else if (currentCount == maxCount) {
            modes.add(node.val); 
        }

        prev = node.val;
        inOrder(node.right);
    }
}

