# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map to look up index of root values in inorder traversal in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            # Base case: no elements to build subtree
            if left > right:
                return None

            # Pick current root from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Root's position in inorder splits left and right subtrees
            in_idx = inorder_map[root_val]

            # Build left subtree first (matches preorder sequence)
            root.left = array_to_tree(left, in_idx - 1)
            # Build right subtree
            root.right = array_to_tree(in_idx + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
