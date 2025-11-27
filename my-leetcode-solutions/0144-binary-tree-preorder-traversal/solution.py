class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return

            result.append(node.val)
            inorder(node.left)
            inorder(node.right)

        inorder(root)
        return result
       
