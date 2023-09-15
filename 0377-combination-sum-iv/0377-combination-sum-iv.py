# https://www.youtube.com/watch?v=dw2nMCxG0ik
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a dictionary dp to store the number of combinations for each total.
        dp = {0: 1}  # There's one way to make a total of 0, which is by choosing nothing.

        # Iterate through the range of totals from 1 to target.
        for total in range(1, target + 1):
            # Initialize the count of combinations for the current total to 0.
            dp[total] = 0
            
            # Iterate through the elements in the nums list.
            for n in nums:
                # Calculate the number of combinations for the current total.
                # Add the number of combinations for (total - n) to dp[total].
                dp[total] += dp.get(total - n, 0)
        
        # Return the number of combinations for the target total.
        return dp[target]
