class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Create a list to store the minimum cost to reach each step.
        dp = [0] * n
        
        # Initialize the first two steps' costs.
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Calculate the minimum cost for each step.
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # The minimum cost to reach the top can be either the last or second-to-last step.
        return min(dp[n - 1], dp[n - 2])
