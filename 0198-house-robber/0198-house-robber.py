#https://www.youtube.com/watch?v=73r3KWiEvyk        

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0    # Initialize previous maximum amount
        rob2 = 0    # Initialize two houses ago maximum amount
        # [rob1,rob2,n,n+1,...]
        for n in nums:
            # Calculate the maximum amount if we choose current house or skip it
            temp = max(n + rob1, rob2)
            rob1 = rob2   # Update previous maximum to the two houses ago
            rob2 = temp   # Update two houses ago to the current maximum
        
        return rob2   # Return the maximum amount that can be robbed
