# link - https://www.youtube.com/watch?v=4RACzI5-du8&t=35s
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0  # Initialize a variable to store the count of palindromic substrings
        for i in range(len(s)):  # Iterate through each character in the string
            l = r = i  # Initialize left and right pointers at the current character
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if the substring s[l:r+1] is a palindrome, and if so, increment the count
                res += 1
                l -= 1  # Move the left pointer to the left
                r += 1  # Move the right pointer to the right

            l = i
            r = i + 1  # Initialize pointers for even-length palindromes

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if the substring s[l:r+1] is a palindrome, and if so, increment the count
                res += 1
                l -= 1  # Move the left pointer to the left
                r += 1  # Move the right pointer to the right
        return res  # Return the total count of palindromic substrings
