class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        if root is None:
            return []
        
        leftSubtree = self.preorderTraversal(root.left)
        rightSubtree = self.preorderTraversal(root.right)

        return [root.val] + leftSubtree + rightSubtree
        
