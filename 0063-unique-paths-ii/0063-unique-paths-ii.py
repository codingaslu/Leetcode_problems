class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Get the number of rows and columns in the obstacle grid
        m = rows = len(obstacleGrid)
        n = cols = len(obstacleGrid[0])

        # Create a 2D DP (dynamic programming) array to store the number of unique paths
        dp = [[0] * cols for _ in range(rows)]

        # Initialize the starting point: If there's an obstacle at the starting point,
        # there are no paths; otherwise, there's one path.
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Populate the DP array for the first column:
        # If there's an obstacle, set the value to 0; otherwise, it's 1 if there was a path from the cell above.
        for i in range(1, m):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1 else 0

        # Populate the DP array for the first row:
        # If there's an obstacle, set the value to 0; otherwise, it's 1 if there was a path from the cell to the left.
        for j in range(1, n):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1 else 0

        # Fill in the DP array for the remaining cells:
        # If there's an obstacle at a cell, set the value to 0.
        # Otherwise, the number of paths to that cell is the sum of paths from the cell above and the cell to the left.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Return the number of unique paths to the bottom-right cell of the grid
        return dp[m - 1][n - 1]
