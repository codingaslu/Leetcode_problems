# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderSuccessor(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        queue = deque([root])
        found = False

        while queue:
            node = queue.popleft()

            if found:
                # If the current node is the Level Order Successor, return it.
                return node

            if node.val == key:
                found = True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # If the key was not found or it's the last node, return None.
        return None
