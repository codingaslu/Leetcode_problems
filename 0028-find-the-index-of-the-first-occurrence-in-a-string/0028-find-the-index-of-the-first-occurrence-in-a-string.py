class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Iterate through 'haystack' to find 'needle'.
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i

        # Return -1 if 'needle' is not found in 'haystack'.
        return -1
