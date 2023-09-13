class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables for result and left/right pointers.
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            # Find the farthest reachable index in the current range.
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # Update left and right pointers for the next jump.
            l = r + 1
            r = farthest
            # Increment the result count.
            res += 1

        return res
