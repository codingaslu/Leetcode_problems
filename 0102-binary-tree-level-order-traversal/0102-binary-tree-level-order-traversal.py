# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []
        from collections import deque
        queue = deque([root])
        while queue:
            ret_row = []
            # fixed size for current level
            for _ in range(len(queue)):
                node = queue.popleft()
                ret_row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(ret_row)
        return ret