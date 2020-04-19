"""
Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k,
whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.


Example 1:

Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.
Example 2:

Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.
Example 3:

Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.


Constraints:
1 <= k <= 10^9
"""

from bisect import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1, 1]
        sum = 1
        """
        generate fibonacci numbers until the last number is less than k, as the sum of n numbers should be
        less than the number given.
        """
        while k > sum:
            sum = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(sum)

        counter = 0
        while k > 0:
            """
            bisect gives where the value has to be inserted in the list, we use -1 of the position
            ie, we subtract the biggest number in fibonacci to minimise the counter. (greedy method)
            """
            index = bisect(fibonacci, k) - 1
            k -= fibonacci[index]
            counter += 1
        return counter

if __name__ == "__main__":
    print(Solution().findMinFibonacciNumbers(19))