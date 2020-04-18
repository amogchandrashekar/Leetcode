"""
Given an array of integers nums, you start with an initial positive value startValue.
In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
"""
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cum_sum = 0
        minimum = 1

        """
        Calculate cumulative sum as shown in the problem description, maintain a variable which tracks the
        minimum cumulative sum. If minimum cumulative sum is less than zero, we need positive equivalent of
        cum_sum + 1 to make the total sum positive. Else, 1 is the least. Hence, return as calculated 
        """
        for num in nums:
            cum_sum += num
            minimum = min(minimum, cum_sum)
        return max(1, 1 - minimum)


if __name__ == "__main__":
    print(Solution().minStartValue([-3, 2, -3, 4, 2]))