# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Helper function to recursively calculate the sum of numbers
        def helper(root: Optional[TreeNode], sum):
            # Base case: If the root is None, return 0
            if not root:
                return 0
            
            # Update the sum by shifting digits left and adding the current node's value
            sum = sum * 10 + root.val

            # If the current node is a leaf node, return the calculated sum
            if root.left is None and root.right is None:
                return sum

            # Recursively calculate the sum for the left and right subtrees
            return helper(root.left, sum) + helper(root.right, sum)
        
        # Start the recursion from the root with an initial sum of 0
        return helper(root, 0)
