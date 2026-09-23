class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftHeight = minDepth(root.left);
        int rightHeight = minDepth(root.right);
        
        if (root.left == null) {
            return rightHeight + 1;
        }        
        if (root.right == null) {
            return leftHeight + 1;
        }        
        return Math.min(leftHeight, rightHeight) + 1;
    }
}

