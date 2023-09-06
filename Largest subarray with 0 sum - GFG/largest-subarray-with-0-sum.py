#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        d={}
        curr_sum=0
        max_length=0
        for i in range(n):
            curr_sum+=arr[i]
            
            if curr_sum in d:
                max_length=max(max_length,i-d[curr_sum])
            elif curr_sum == 0:
                max_length=i+1
            else:
                d[curr_sum] = i
        return max_length

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends