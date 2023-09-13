# This class defines a Solution with a method hIndex, which calculates the H-index of a given list of citations.
class Solution:
    def hIndex(self, c: List[int]) -> int:
        # Sort the list in descending order.
        c.sort(reverse=True)
        
        # If there's only one citation and it's greater than zero, the H-index is 1.
        if len(c) == 1 and c[0] > 0:
            return 1
        
        # If the lowest citation value is greater than or equal to the number of citations,
        # the H-index is equal to the number of citations.
        if c[-1] >= len(c):
            return len(c)
        
        # Otherwise, iterate through the sorted list of citations and find the H-index.
        for i in range(len(c)):
            if c[i] < i + 1:
                return i
        
        # If no H-index is found, return 0.
        return 0
