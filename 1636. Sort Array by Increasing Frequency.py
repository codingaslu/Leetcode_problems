# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

 

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]
 


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sort=[]
        d={i:0 for i in set(nums) }
        for i in nums:
            d[i]=d[i]+1
        sorted_d = dict(sorted(d.items(), key=lambda item: (item[1],-item[0])))
        # print(sorted_d)
        for i in sorted_d.keys():
            for j in range(sorted_d[i]):
                sort.append(i)
        return sort


# Another Method

        # dic = {}
        # for v in nums:
        #     dic[v] = dic.get(v,0) + 1
        
        # stack = sorted(dic.items(), key = lambda x: (x[1],-x[0]))
        # ans = []
        # for key,freq in stack:
        #     while freq:
        #         ans.append(key)
        #         freq -= 1
        
        # return ans
