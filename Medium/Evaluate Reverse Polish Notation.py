from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = deque()
        symbols = ["+", "-", "*", "/"]

        for char in tokens:
            if char in symbols and len(queue) >= 2:
                dr = queue.pop()
                nr = queue.pop()
                if char == '+':
                    res = nr + dr
                elif char == '-':
                    res = nr - dr
                elif char == '*':
                    res = nr * dr
                elif char == '/':
                    res = int(nr / dr)
                queue.append(res)

            else:
                queue.append(int(char))

        return queue.pop()


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))