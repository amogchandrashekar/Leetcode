from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_set = set()
        ans = list()

        for i in range(len(s) - 9):
            if s[i: i + 10] in hash_set and s[i: i + 10] not in ans:
                ans.append(s[i: i + 10])
            hash_set.add(s[i: i + 10])

        return ans


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))