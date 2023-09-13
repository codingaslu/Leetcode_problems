#link - https://www.youtube.com/watch?v=bNvIQI2wAjk

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Initialize an array to store the results.
    res = [1] * len(nums)
      
    # Calculate the prefix products and store them in the 'res' array.
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    # Calculate the postfix products and update the 'res' array.
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i] 
    
    # Return the final result.
    return res
