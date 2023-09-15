# https://www.youtube.com/watch?v=Sx9NNgInc3A&t=650s
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Create a dynamic programming (DP) array to store subproblem results.
        dp = [False] * (len(s) + 1)
        
        # Initialize the DP array. dp[i] will be True if s[i:] can be segmented.
        dp[len(s)] = True

        # Iterate through the string s in reverse order.
        for i in range(len(s) - 1, -1, -1):
            # Iterate through each word in the wordDict.
            for w in wordDict:
                # Check if it's possible to break the string from the current position (i)
                # using the word (w) from wordDict.
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Update dp[i] based on subproblem result.
                
                # If dp[i] is True (i.e., s[i:] can be segmented), no need to check other words.
                if dp[i]:
                    break
        
        # The final result is stored in dp[0], which represents whether the entire string can be segmented.
        return dp[0]

            


        