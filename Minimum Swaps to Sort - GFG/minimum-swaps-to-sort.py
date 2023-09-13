

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
        n = len(nums)
        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort()  # Sort the pairs based on element values
    
        visited = [False] * n  # Initialize a visited array to keep track of visited elements
        swaps = 0  # Initialize the number of swaps
    
        for i in range(n):
            # If the element is already visited or in its correct position
            if visited[i] or pairs[i][1] == i:
                continue
    
            cycle_size = 0
            j = i
    
            while not visited[j]:
                visited[j] = True
                j = pairs[j][1]
                cycle_size += 1
    
            if cycle_size > 0:
                swaps += (cycle_size - 1)
    
        return swaps


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends