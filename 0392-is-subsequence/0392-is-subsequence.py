class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        r=0

        for i in range(len(t)):
            if r == len(s):
                return True
            if t[l] == s[r]:
                r+=1
            l+=1
        return r == len(s)