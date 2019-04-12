# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

class Solution:
    def arrayPairSum(self, nums):
        """
        Function which takes a list as input and returns maximum sum of various combinations
        :param nums: list of numbers
        """
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    print(Solution().arrayPairSum([1,2,3,4]))