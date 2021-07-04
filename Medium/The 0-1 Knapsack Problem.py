class Solution:
    def knapsack(self, values, weights, maxWeightConstraint):
        """
        :type values: list of int
        :type weights: list of int
        :type maxWeightConstraint: int
        :rtype: int
        """
        memo = dict()

        def dfs(rem_weight, ind):

            if (rem_weight, ind) in memo:
                return memo[(rem_weight, ind)]

            if ind >= len(weights) or rem_weight == 0:
                return 0

            if weights[ind] <= rem_weight:
                memo[(rem_weight, ind)] = max(values[ind] + dfs(rem_weight - weights[ind], ind + 1), dfs(rem_weight, ind + 1))
            else:
                memo[(rem_weight, ind)] = dfs(rem_weight, ind + 1)

            return memo[(rem_weight, ind)]

        return dfs(maxWeightConstraint, 0)


if __name__ == '__main__':
    values = [60, 100, 120, 80, 30]
    weights = [10, 20, 30, 40, 50]
    maxWeight = 400
    print(Solution().knapsack(values, weights, maxWeight))