from itertools import product


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        perms = set()
        all_prods = product(map(str, range(n)), repeat=k)
        for permutation in all_prods:
            perms.add(''.join(permutation))

        res = []

        def dfs(cur_state):
            if not perms:
                return

            for digit in map(str, range(n)):
                next_state = cur_state + digit
                next_state = next_state[1:]

                if next_state in perms:
                    perms.remove(next_state)
                    dfs(next_state)
                    res.append(digit)

        start_state = '0' * n
        perms.remove(start_state)
        dfs(start_state)
        return ''.join(res) + start_state


if __name__ == '__main__':
    n = 2
    k = 2
    print(Solution().crackSafe(n, k))