# link:-https://www.youtube.com/watch?v=L27_JpN6Z1Q&t=1214s
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Create a 2D array 'dp' with rows representing different coin denominations
        # and columns representing amounts from 0 to 'amount'.
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        
        # Base case: To make 0 amount, there is only one way, which is to use no coins.
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        # Fill the 'dp' table using a bottom-up approach.
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # If the current coin denomination can be used, 
                    # there are two options: (1) Use the current coin and subtract its value,
                    # (2) Don't use the current coin and take the value from the row above.
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    # If the current coin denomination is too large to be used for the current amount,
                    # take the value from the row above.
                    dp[i][j] = dp[i - 1][j]
        
        # The final value in dp[len(coins)][amount] represents the number of combinations to make up the given amount.
        return dp[len(coins)][amount]
