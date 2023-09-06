class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        global_sum = float('-inf')
        local_sum = 0
        
        for num in A:
            local_sum = max(num,local_sum+num)
            global_sum = max(local_sum,global_sum)
        
        return global_sum
