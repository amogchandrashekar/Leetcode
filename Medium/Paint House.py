class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0

        for ind in range(1, len(costs)):
            for paint in range(len(costs[ind])):
                costs[ind][paint] += min(costs[ind - 1][i] for i in range(3) if i != paint)

        return min(costs[-1])