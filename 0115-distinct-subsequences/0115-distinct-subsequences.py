#https://www.youtube.com/watch?v=-RDzMJ33nx8
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}  # Initialize a cache to store results.

        def dfs(i, j):
            if j == len(t):  # If t is fully matched, return 1.
                return 1
            if i == len(s):  # If s is exhausted, return 0.
                return 0
            if (i, j) in cache:  # Check if result is already cached.
                return cache[(i, j)]

            if s[i] == t[j]:  # If current chars match:
                # 1. Include current char in s and move forward in both s and t.
                # 2. Skip current char in s and continue matching t.
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:  # If current chars don't match, skip current char in s.
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]  # Return the computed result.

        return dfs(0, 0)  # Start matching from the beginning of both s and t.
