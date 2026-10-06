class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    total_sum = 0

    def reverse_inorder(node: TreeNode | None):
      nonlocal total_sum
      if not node:
        return

      reverse_inorder(node.right)
      total_sum += node.val
      node.val = total_sum
      reverse_inorder(node.left)

    reverse_inorder(root)
    return root
