from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()

        l, r = 0, 0
        max_len = 0

        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    basket.pop(fruits[l])
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


if __name__ == '__main__':
    fruits = [1, 2, 3, 2, 2]
    print(Solution().totalFruit(fruits))
