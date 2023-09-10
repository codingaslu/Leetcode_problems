#link -https://www.youtube.com/watch?v=pGMsrvt0fpk
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Create a 2D list 'dp' to store the minimum path sum for each cell.
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

        # Initialize the bottom-right cell of 'dp' to 0, as it represents the destination.
        dp[rows - 1][cols] = 0

        # Starting from the bottom-right cell, iterate through the grid.
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # Calculate the minimum path sum for the current cell by adding the current cell's value
                # to the minimum of the path sums from the cell below (dp[r+1][c]) and the cell to the right (dp[r][c+1]).
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        # The top-left cell of 'dp' now contains the minimum path sum from the top-left to the bottom-right cell of the grid.
        return dp[0][0]
