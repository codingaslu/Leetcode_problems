# link-https://www.youtube.com/watch?v=1IL5sxfoA-I
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Create a 2D array dp to store the minimum path sums.
        dp = [[0] * len(row) for row in triangle]
        
        # Initialize the bottom row of dp with the values from the bottom of the triangle.
        dp[-1] = triangle[-1]

        # Start from the second-to-last row and work our way up.
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # For each element, calculate the minimum path sum from this point down.
                dp[row][col] = triangle[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])

        # The minimum path sum will be the value at the top of the dp array.
        return dp[0][0]

        