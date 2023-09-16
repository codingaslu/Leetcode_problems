class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        



        # local_area = 0
        # global_area = 0
        # n = len(height)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         h = min(height[i], height[j])
        #         w = j - i
        #         local_area = h * w
        #         global_area = max(global_area, local_area)

        # return global_area
