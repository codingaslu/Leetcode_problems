class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j, ans = 0, 0, 0
        zero_count = 0  # Initialize a variable to count zeros

        def invalid():
            return zero_count > 1  # Function to check if the window is invalid (more than one zero)

        while j < len(nums):
            # Update state based on A[j] (the current element in the array)
            if nums[j] == 0:
                zero_count += 1
            
            # Check if the window is invalid, and if so, shrink the left edge
            while invalid():
                # Update state using A[i] (the element at the left edge)
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            
            # Calculate and update the maximum subarray length found thus far
            ans = max(ans, j - i + 1)
            
            j += 1

        # Subtract 1 from the maximum subarray length to account for the one element to be deleted
        return ans - 1
