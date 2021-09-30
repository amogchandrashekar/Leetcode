from collections import defaultdict, Counter, deque
import heapq


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        in_node = {node: 0 for seq in seqs for node in seq}

        if len(in_node) != len(org):
            return False

        adj_list = defaultdict(set)
        for seq in seqs:
            for ind in range(len(seq) - 1):
                src, dst = seq[ind], seq[ind + 1]
                if dst in adj_list[src]:
                    continue
                adj_list[src].add(dst)
                in_node[dst] += 1

        queue = deque([node for node, count in in_node.items() if count == 0])
        reconstructed = []

        while queue:
            node = queue.pop()
            reconstructed.append(node)

            if queue:
                return False

            for adj_node in adj_list[node]:
                in_node[adj_node] -= 1
                if in_node[adj_node] == 0:
                    queue.append(adj_node)

        return reconstructed == org


if __name__ == '__main__':
    org = [1]
    seqs = [[1],[2,3],[3,2]]
    print(Solution().sequenceReconstruction(org, seqs))
