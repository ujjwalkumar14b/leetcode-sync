class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorder(node.right)
            result.append(node.val)

        inorder(root)
        return result
       
