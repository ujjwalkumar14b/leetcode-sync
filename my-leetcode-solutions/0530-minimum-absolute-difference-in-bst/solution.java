class Solution {

    private int minDiff = Integer.MAX_VALUE;
    private Integer prev = null;

    public int getMinimumDifference(TreeNode root) {
        inOrder(root);
        return minDiff;
    }

    private void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        inOrder(node.left);

        if (prev != null) {
            minDiff = Math.min(minDiff, node.val - prev);
        }
        prev = node.val;
        inOrder(node.right);
    }
}

