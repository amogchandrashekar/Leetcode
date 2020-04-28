"""
Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        circular = nums + nums
        length = len(nums)
        for index, num in enumerate(circular):
            while stack and stack[-1][-1] < num:
                ind, n = stack.pop()
                res[int(ind % length)] = num
            stack.append([index, num])
        return res


if __name__ == "__main__":
    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    print(Solution().nextGreaterElements(nums))
