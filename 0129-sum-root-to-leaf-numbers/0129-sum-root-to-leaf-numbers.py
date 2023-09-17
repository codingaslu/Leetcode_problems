# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

    
        def helper(root: Optional[TreeNode],sum):
            
            if not root:
                return 0
            
            sum= sum*10 + root.val

            if root.left == None and root.right == None:
                return sum

            return helper(root.left,sum) + helper(root.right,sum)
        
        return helper(root,0)