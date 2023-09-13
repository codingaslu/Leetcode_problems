link-https://www.youtube.com/watch?v=PfkBS9qIMRE&list=PLdo5W4Nhv31aBrJE1WS4MR9LRfbmZrAQu&index=5
# Knapsack Problem

## Problem Description

Given two integer arrays `A` and `B` of size `N` each, which represent values and weights associated with `N` items respectively.

Also given an integer `C` which represents the knapsack capacity.

Find out the maximum value subset of `A` such that the sum of the weights of this subset is smaller than or equal to `C`.

**NOTE:**

You cannot break an item, either pick the complete item, or don't pick it (0-1 property).

### Problem Constraints

- `1 <= N <= 103`
- `1 <= C <= 103`
- `1 <= A[i], B[i] <= 103`

## Input Format

The input consists of the following:

- First argument is an integer array `A` of size `N` denoting the values of `N` items.
- Second argument is an integer array `B` of size `N` denoting the weights of `N` items.
- Third argument is an integer `C` denoting the knapsack capacity.

## Output Format

Return a single integer denoting the maximum value subset of `A` such that the sum of the weights of this subset is smaller than or equal to `C`.

## Example Input

**Input 1:**


A = [60, 100, 120]
B = [10, 20, 30]
C = 50

Example Explanation
Explanation 1:

 Taking items with weight 20 and 30 will give us the maximum value i.e 100 + 120 = 220
Explanation 2:

 Knapsack capacity is 10 but each item has weight greater than 10 so no items can be considered in the knapsack therefore answer is 0.

                

```python
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    
    # A - Values
    # B - Weights
    # C - Capacity
    def solve(self, A, B, C):
        n = len(A)
        
        # Initialize the dp array with zeros for a capacity of 0.
        dp = [[0] * (C + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, C + 1):
                if B[i - 1] <= j:
                    # If the current item's weight is less than or equal to the current capacity,
                    # we have a choice to either include it or exclude it.
                    # We choose the maximum value between these two options.
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - B[i - 1]] + A[i - 1])
                else:
                    # If the current item's weight is greater than the current capacity,
                    # we can't include it in the knapsack, so we retain the previous maximum value.
                    dp[i][j] = dp[i - 1][j]
                
        return dp[n][C]
