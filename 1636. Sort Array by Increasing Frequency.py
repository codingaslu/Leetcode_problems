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
