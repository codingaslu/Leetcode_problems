class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        i = 0
        while i < length:
            a = nums.count(nums[i])
            if a > 2:
                nums.pop(i)
                length -= 1
            else:
                i += 1

        return len(nums)

        # Another merthod


        # lis=[]
        # for i in nums:
        #     if lis.count(i)<2:
        #         lis.append(i)
        # nums.clear()
        # nums.extend(lis)
        # return len(nums)

