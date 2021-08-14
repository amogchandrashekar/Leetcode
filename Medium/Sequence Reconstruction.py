from collections import defaultdict, Counter
import heapq


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # write your code here
        in_node = Counter()
        adj_list = defaultdict(list)

        for seq in seqs:
            for ind in range(len(seq) - 1):
                if seq[ind + 1] not in adj_list[seq[ind]]:
                    adj_list[seq[ind]].append(seq[ind + 1])
                    in_node[seq[ind + 1]] += 1
                    in_node[seq[ind]] += 0
            if seq:
                adj_list[seq[-1]].extend([])
                in_node[seq[-1]] += 0

        seen = set()
        heap = list()
        order = list()

        for node, in_nodes in in_node.items():
            heapq.heappush(heap, [in_nodes, node])

        while heap:
            in_nodes, node = heapq.heappop(heap)

            if node in seen:
                continue

            order.append(node)
            seen.add(node)

            if in_nodes != 0:
                return False

            if heap and heap[0][0] == 0:
                # checking for no contender
                return False

            for adj_node in adj_list[node]:
                in_node[adj_node] -= 1
                heapq.heappush(heap, [in_node[adj_node], adj_node])

        return order == org


if __name__ == '__main__':
    org = [1]
    seqs = []
    print(Solution().sequenceReconstruction(org, seqs))
