# 159. Longest Substring with At Most Two Distinct Characters (Medium)
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.


def lengthOfLongestSubstring(s: str) -> int:
    # write your code here
    i=0
    j=0
    ans=0
    ch={}

    def invalid():
        return len(ch) > 2 and i <= j

    while(j<len(s)):
        ch[s[j]] = ch.get(s[j], 0) + 1

        while invalid():
            ch[s[i]]-=1
            if ch[s[i]] == 0:
                del ch[s[i]]
            i+=1

        ans=max(ans,j-i+1)
        j+=1
        
    return ans

