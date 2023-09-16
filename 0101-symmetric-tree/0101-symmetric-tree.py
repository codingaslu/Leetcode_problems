# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check if the root is None, and if so, it's symmetric.
        if not root:
            return True
        
        from collections import deque

        # Create a queue to perform a level-order traversal.
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
            # Pop the left and right nodes from the queue for comparison.
            left = queue.popleft()  
            right = queue.popleft()

            # If both nodes are None, continue to the next pair.
            if left ==  None and right == None:
                continue
                
            # If one node is None and the other is not, the tree is not symmetric.
            if left == None and right != None:
                return False
                
            if left != None and right == None:
                return False                

            # If the values of left and right nodes are not the same, the tree is not symmetric.
            if left.val != right.val:
                return False

            # Add the left and right children of the current nodes to the queue for further comparison.
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        # If the loop completes without finding asymmetry, the tree is symmetric.
        return True
