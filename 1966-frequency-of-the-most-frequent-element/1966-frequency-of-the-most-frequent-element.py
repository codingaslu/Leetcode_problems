class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        # Sort the input list A
        A.sort()
        i = 0  # Left pointer of the window
        j = 0  # Right pointer of the window
        N = len(A)  # Length of the list A
        summation = 0  # Sum of elements in the current window
        max_freq = 0  # Maximum frequency found so far

        # Define the invalid condition for the window
        def invalid():
            return (j - i + 1) * A[j] - summation > k

        while j < N:
            summation += A[j]  # Add the current element to the window sum
            while invalid():
                summation -= A[i]  # Remove the leftmost element from the window
                i += 1  # Move the left pointer to the right
            max_freq = max(max_freq, j - i + 1)  # Update the maximum frequency
            j += 1  # Move the right pointer to the right

        return max_freq  # Return the maximum frequency


        

