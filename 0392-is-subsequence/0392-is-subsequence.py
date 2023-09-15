class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0  # Initialize a pointer 'l' for string 't'.
        r = 0  # Initialize a pointer 'r' for string 's'.

        for i in range(len(t)):  # Iterate through characters in string 't'.
            if r == len(s):  # If all characters in 's' have been matched, return True.
                return True
            if t[l] == s[r]:  # If the current character in 't' matches the current character in 's', move 'r' forward.
                r += 1
            l += 1  # Move 'l' forward to check the next character in 't'.

        return r == len(s)  # Return True if all characters in 's' have been matched, otherwise, return False.
