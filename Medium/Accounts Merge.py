from collections import defaultdict


class DSU:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, group_id):
        while group_id != self.parent[group_id]:
            # path compression
            self.parent[group_id] = self.parent[self.parent[group_id]]
            group_id = self.parent[group_id]
        return group_id

    def union(self, groupa, groupb):
        par_a, par_b = self.find(groupa), self.find(groupb)

        # parents are same. no need for union
        if par_a == par_b:
            return

        # union by rank
        rank_a, rank_b = self.rank[par_a], self.rank[par_b]
        if rank_a < rank_b:
            self.parent[par_a] = par_b
        elif rank_b < rank_a:
            self.parent[par_b] = par_a
        else:
            self.rank[par_a] += 1
            self.parent[par_b] = par_a


class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU(len(accounts))

        email_id_to_group = dict()
        for group_id in range(len(accounts)):
            name, emails = accounts[group_id][0], accounts[group_id][1:]
            for email in emails:
                if email not in email_id_to_group:
                    email_id_to_group[email] = group_id
                else:
                    dsu.union(email_id_to_group[email], group_id)

        unioned_groups = defaultdict(set)
        for group_id in range(len(accounts)):
            unioned_groups[dsu.find(group_id)] |= set(accounts[group_id][1:])

        # get it in required format
        res = list()
        for group_id in sorted(unioned_groups):
            sorted_list = sorted(list(unioned_groups[group_id]))
            user_name = accounts[group_id][0]
            res.append([user_name] + sorted_list)

        return res


if __name__ == '__main__':
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(Solution().accountsMerge(accounts))
