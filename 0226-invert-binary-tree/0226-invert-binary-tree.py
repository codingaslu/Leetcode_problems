# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Invert the left and right subtrees recursively
        left_inverse = self.invertTree(root.left)
        right_inverse = self.invertTree(root.right)

        # Swap the left and right subtrees
        root.left, root.right = right_inverse, left_inverse

        return root
