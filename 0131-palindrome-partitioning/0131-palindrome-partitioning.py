# link-https://www.youtube.com/watch?v=3jvWodd7ht0
# link-https://www.youtube.com/watch?v=pkBG7lB-1N8
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # List to store the final result (list of lists of palindromic substrings)
        part = []  # List to store the current partition being constructed

        # Helper function to check if a substring is a palindrome
        def is_palind(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Recursive function to find all valid partitions starting from index i
        def dfs(i):
            if i == len(s):  # If we've reached the end of the string, add the current partition to the result
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if is_palind(s, i, j):  # Check if the substring is a palindrome
                    part.append(s[i:j + 1])  # Add the palindrome substring to the current partition
                    dfs(j + 1)  # Recursively call dfs for the next index
                    part.pop()  # Backtrack by removing the last added element from the partition

        dfs(0)  # Start the DFS search from the beginning of the string
        return res  # Return the list of all valid partitions
