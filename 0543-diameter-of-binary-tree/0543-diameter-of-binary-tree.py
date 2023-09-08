# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0  # Return 0 for an empty subtree

            # Recursively calculate the heights of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the maximum diameter found so far
            self.diameter = max(self.diameter, left_height + right_height)

            # Return the height of the current subtree (maximum of left and right heights)
            return max(left_height, right_height) + 1

        self.diameter = 0  # Initialize the diameter to 0
        dfs(root)  # Start the depth-first traversal
        return self.diameter





