class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        A= nums
        A.sort()
        i=0
        j=0
        N=len(A)
        summation = 0
        max_freq = 0

        def invalid():
            return A[j] * (j - i + 1) > summation +k

        while j<N:
            summation+=A[j]
            while invalid():
                summation-=A[i]
                i+=1
            max_freq = max(max_freq,j-i+1)
            j+=1
        return max_freq


