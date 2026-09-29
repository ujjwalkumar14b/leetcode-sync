class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:

        if root is None:
            return []
        
        leftSubtree = self.inorderTraversal(root.left)
        rightSubtree = self.inorderTraversal(root.right)

        return leftSubtree + [root.val] + rightSubtree
        

