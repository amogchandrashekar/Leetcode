from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        differences = defaultdict(list)
        for string in strings:
            cur_key = list()
            for ind in range(len(string) - 1):
                cur_char = string[ind]
                next_char = string[ind + 1]
                diff = (ord(next_char) - ord(cur_char)) % 26
                cur_key.append(diff)
            differences[tuple(cur_key)].append(string)
        return list(differences.values())