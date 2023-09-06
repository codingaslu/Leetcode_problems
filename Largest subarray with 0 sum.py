# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.

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
