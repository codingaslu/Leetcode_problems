#link-https://www.youtube.com/watch?v=J2eoCvk59Rc
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a 2D array 'dp' with rows representing different coin denominations
        # and columns representing amounts from 0 to 'amount'.
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]
        
        # Base case: To make 0 amount, no coins are needed.
        for i in range(len(coins) + 1):
            dp[i][0] = 0
        
        # Fill the 'dp' table using a bottom-up approach.
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # Calculate the minimum number of coins needed for the current amount.
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    # If the current coin denomination is too large, take the value from the row above.
                    dp[i][j] = dp[i - 1][j]
        
        # If dp[len(coins)][amount] is still 'inf', it means it's not possible to make up the amount.
        return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1
