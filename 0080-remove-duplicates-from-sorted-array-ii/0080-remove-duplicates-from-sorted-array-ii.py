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
        
        for i in range(length, len(nums)):
            nums.pop()

        return len(nums)
