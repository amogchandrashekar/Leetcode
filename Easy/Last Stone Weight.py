"""

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""
import heapq


class Solution:
    def laststoneweight(self, stones):
        """
        Find last stone after smashing
        :param stones: list of integers, representing weight of stones
        :return: Last stone remaining or zero
        """
        stones = [-stone for stone in stones] # Convert to negative (because heapq is binary min heap implementation)
        heapq.heapify(stones)
        while len(stones) > 1:
            largest, second_largest = heapq.heappop(stones), heapq.heappop(stones)
            diff = largest - second_largest
            if diff != 0:
                heapq.heappush(stones, diff)
        return -stones[0] if stones else 0


if __name__=="__main__":
    stones = [2, 2]
    print(Solution().laststoneweight(stones))