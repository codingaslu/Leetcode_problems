class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[char.lower() for char in s if char.isalnum()]
        
        return a == a[::-1]
        