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


        

def maxValidWindow(A, N):
    i = 0
    j = 0
    ans = 0
    
    def invalid():
        # Define your invalid condition here
        # This function should return True if the window is invalid, False otherwise
        pass

    while j < N:
        # CODE: Use A[j] to update state which might make the window invalid
        if invalid():
            # When invalid, keep shrinking the left edge until it's valid again
            # CODE: Update state using A[i]
            i += 1
        else:
            ans = max(ans, j - i + 1)  # The window [i, j] is the maximum window found thus far
            j += 1
    
    return ans


