# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Initialize an empty list to store the averages of each level.
        averages = []

        # Check if the root node is None (empty tree), and return an empty list if so.
        if not root:
            return []

        # Initialize a queue with the root node.
        queue = deque([root])

        # Perform a level-order traversal of the binary tree.
        while queue:
            level_sum = 0
            level_count = len(queue)

            # Iterate through all nodes at the current level.
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                # Add the left and right children to the queue if they exist.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the average value for the current level and append it to the result list.
            averages.append(level_sum / level_count)

        # Return the list of level averages.
        return averages
