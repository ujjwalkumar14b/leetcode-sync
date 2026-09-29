class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        if root is None:
            return []
        
        leftSubtree = self.postorderTraversal(root.left)
        rightSubtree = self.postorderTraversal(root.right)

        return leftSubtree + rightSubtree + [root.val]
        
