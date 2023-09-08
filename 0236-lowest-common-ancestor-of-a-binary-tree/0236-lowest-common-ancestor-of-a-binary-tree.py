# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        if root == p or root == q:
            return root

        node_left = self.lowestCommonAncestor(root.left,p,q)
        node_right = self.lowestCommonAncestor(root.right,p,q)

        if node_left !=None and node_right!=None:
            return root
        
        if node_left != None:
            return node_left
        else:
            return node_right
