# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        

        from collections import deque

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)

        while queue:
                left = queue.popleft()  
                right = queue.popleft()

                if left ==  None and right == None:
                    continue
                
                if left == None and right != None:
                    return False
                
                if left != None and right == None:
                    return False                

                if left.val != right.val:
                    return False

                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)

        return True








        