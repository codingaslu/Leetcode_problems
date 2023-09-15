#https://www.youtube.com/watch?v=73r3KWiEvyk        
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0    # Initialize the variable to store the maximum amount robbed from the previous house
        rob2 = 0    # Initialize the variable to store the maximum amount robbed from two houses ago
        
        # [rob1,rob2,n,n+1,...]
        # Iterate through the list of house values
        for n in nums:
            temp = max(n + rob1, rob2)  # Calculate the maximum amount that can be robbed if we choose the current house or skip it
            rob1 = rob2               # Update rob1 to the previous rob2 value (moving it one step ahead)
            rob2 = temp               # Update rob2 to the newly calculated maximum value
        
        return rob2   # Return the maximum amount that can be robbed after iterating through all the houses

        