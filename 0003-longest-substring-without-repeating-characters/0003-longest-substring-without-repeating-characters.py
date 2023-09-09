class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        ch = {char: 0 for char in s}
        n = len(s)

        def invalid(j):
            return ch[s[j]] > 1

        while j < n:
            ch[s[j]] += 1
            while invalid(j):
                ch[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans
