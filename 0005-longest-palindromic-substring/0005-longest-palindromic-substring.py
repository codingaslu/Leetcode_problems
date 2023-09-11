class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables to store the longest palindrome and its length
        res = ""
        resLen = 0
        length = 0
        
        # Loop through the characters in the input string 's'
        for i in range(len(s)):
            # Check for palindromes with odd length (centered at 'i')
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1  # Calculate the length of the current palindrome
                if resLen < length:
                    resLen = length
                    res = s[l:r + 1]  # Update the longest palindrome substring
                l -= 1
                r += 1
            
            # Check for palindromes with even length (centered between 'i' and 'i+1')
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1  # Calculate the length of the current palindrome
                if resLen < length:
                    resLen = length
                    res = s[l:r + 1]  # Update the longest palindrome substring
                l -= 1
                r += 1

        return res  # Return the longest palindrome found
