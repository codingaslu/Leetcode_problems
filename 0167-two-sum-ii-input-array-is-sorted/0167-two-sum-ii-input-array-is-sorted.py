class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0  # Initialize the left pointer
        right = len(numbers) - 1  # Initialize the right pointer
        
        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]  # Calculate the current sum of elements at left and right positions

            if sum == target:
                return [left + 1, right + 1]  # If the sum equals the target, return the indices
            elif sum > target:
                right -= 1  # If the sum is greater than the target, move the right pointer to the left
            else:
                left += 1  # If the sum is less than the target, move the left pointer to the right

        # Return an empty list if no solution is found
        return []
 

        # brute force
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1,j+1]