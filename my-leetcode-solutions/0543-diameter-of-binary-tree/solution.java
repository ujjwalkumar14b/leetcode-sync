class Solution {
    static class Info {
        int diameter;
        int height;

        Info(int diameter, int height) {
            this.diameter = diameter;
            this.height = height;
        }
    }

    public int diameterOfBinaryTree(TreeNode root) {
        return getTreeInfo(root).diameter;
    }

    private Info getTreeInfo(TreeNode root) {
        if (root == null) {
            return new Info(0, 0);
        }

        Info leftInfo = getTreeInfo(root.left);
        Info rightInfo = getTreeInfo(root.right);

        int currentDiameter = leftInfo.height + rightInfo.height;
        int maxDiameterSoFar = Math.max(
            Math.max(leftInfo.diameter, rightInfo.diameter), 
            currentDiameter
        );

        int height = Math.max(leftInfo.height, rightInfo.height) + 1;

        return new Info(maxDiameterSoFar, height);
    }
}

