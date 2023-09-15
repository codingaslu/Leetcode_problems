#https://www.youtube.com/watch?v=rWAJCfYYOvM
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Start by comparing two cases:
        # 1. Rob the first house and consider the remaining houses from index 2 onward.
        # 2. Skip the first house and consider all the houses from index 1 onward.
        # The maximum of these two cases will be the result.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1 = 0  # Maximum amount robbed from the previous house
        rob2 = 0  # Maximum amount robbed from the house before the previous house

        for n in nums:
            # Calculate the maximum amount that can be robbed at the current house:
            newRob = max(n + rob1, rob2)

            # Update rob1 and rob2 for the next iteration:
            rob1 = rob2
            rob2 = newRob

        # The final value of rob2 will represent the maximum amount that can be robbed.
        return rob2
