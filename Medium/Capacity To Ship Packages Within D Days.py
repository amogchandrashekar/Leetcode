from typing import List
from copy import deepcopy


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        min_weight = max(weights)
        max_weight = sum(weights)

        ans = deepcopy(max_weight)

        def number_of_days_with_shipsize(ship_size):
            days = 1
            cur_weight = 0

            for weight in weights:
                cur_weight += weight
                if cur_weight > ship_size:
                    cur_weight = weight
                    days += 1

            return days

        while min_weight <= max_weight:

            ship_size = (min_weight + max_weight) // 2
            required_days = number_of_days_with_shipsize(ship_size)

            if required_days <= days:
                ans = ship_size
                max_weight = ship_size - 1
            else:
                min_weight = ship_size + 1

        return ans


if __name__ == '__main__':
    weights = [1,2,3,1,1]
    days = 4
    print(Solution().shipWithinDays(weights, days))