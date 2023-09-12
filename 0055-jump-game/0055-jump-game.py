#https://www.youtube.com/watch?v=Yan0cv2cLy8
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the goal as the last index of the input list
        goal = len(nums) - 1

        # Iterate through the list in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # If we can jump from the current position (i) to the goal or beyond,
            # update the goal to the current position (i)
            if i + nums[i] >= goal:
                goal = i

        # If we reach the beginning of the list (goal is 0), it means we can jump
        # from the start to the end, so return True. Otherwise, return False.
        return True if goal == 0 else False
