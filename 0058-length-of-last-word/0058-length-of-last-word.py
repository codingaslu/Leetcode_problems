class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing whitespaces
        s = s.strip()
        
        # Initialize variables
        n = len(s)
        count = 0
        
        # Iterate from the end of the string
        for i in range(n-1, -1, -1):
            if s[i] == " ":
                break
            count += 1
        
        # Return the count, which represents the length of the last word
        return count
