class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;
        return findSecondMin(root, root.val);
    }

    private int findSecondMin(TreeNode node, int rootVal) {
        if (node == null) return -1;
        
        if (node.val > rootVal) return node.val;
        
        int left = findSecondMin(node.left, rootVal);
        int right = findSecondMin(node.right, rootVal);
        
        if (left != -1 && right != -1) {
            return Math.min(left, right);
        }
        
        return left != -1 ? left : right;
    }
}

