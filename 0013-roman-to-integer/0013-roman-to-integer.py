class Solution:
    def romanToInt(self, s: str) -> int:
        
        res=0

        transilations= { "I" : 1, "V" : 5, "X" : 10 , "L" : 50, "C" : 100 , "D" : 500 , "M" : 1000   }
        
        n=len(s)
        
        for i in range(n):
            if i+1 < n and transilations[s[i]] < transilations[s[i+1]]:
                res -= transilations[s[i]]
            else:
                res += transilations[s[i]]  

        return res
                
