class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0          # Left pointer of the sliding window
        j = 0          # Right pointer of the sliding window
        ans = 0        # Count of valid subarrays
        product = 1    # Current product of elements in the window
        n = len(nums)  # Length of the input list

        # Handle the edge case when k is 0 (no valid subarrays)
        if k == 0:
            return 0

        # Function to check if the current window is invalid
        def invalid():
            return product >= k and i <= j

        # Iterate through the list nums using the right pointer j
        while j < n:
            product *= nums[j]  # Update the product by multiplying with nums[j]

            # While the window is invalid, shrink it from the left
            while invalid():
                product /= nums[i]  # Divide by nums[i] to make the window valid again
                i += 1             # Move the left pointer to the right

            ans += (j - i + 1)     # Update the count of valid subarrays
            j += 1                 # Move the right pointer to the right

        return ans  # Return the total count of valid subarrays
