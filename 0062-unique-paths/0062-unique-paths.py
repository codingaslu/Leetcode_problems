# link :- https://www.youtube.com/watch?v=rQp40nkjdT8&list=PLvhVqTAG_P3IB4O5AjnM4p-YYbiIQ649s&index=27
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Initialize a 2D array (dp) to store the number of unique paths for each cell.
        dp = [[0] * n for _ in range(m)]

        # Starting point (top-left corner) has only one unique path to itself.
        dp[0][0] = 1
        
        # Initialize the number of unique paths for all cells in the first column to 1,
        # since there's only one way to reach any cell in the first column (by moving downwards).
        for i in range(m):
            dp[i][0] = 1
        
        # Initialize the number of unique paths for all cells in the first row to 1,
        # since there's only one way to reach any cell in the first row (by moving right).
        for j in range(n):
            dp[0][j] = 1

        # Calculate the number of unique paths for each cell in the grid using dynamic programming.
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to a cell is the sum of paths from the cell above and the cell to the left.
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is stored in the bottom-right corner of the grid.
        # It represents the total number of unique paths to reach the destination cell.
        return dp[m - 1][n - 1]
