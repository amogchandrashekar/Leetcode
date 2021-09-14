from typing import List


class Solution:
    # time: O(m + n)
    # space : O(m + n)

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = dict()

        for key, val in knowledge:
            knowledge_dict[key] = val

        s = s.split('(')
        ans = s[0]

        for split_words in s[1:]:
            bracket_enclosed, remaining = split_words.split(')')
            ans += knowledge_dict.get(bracket_enclosed, "?")
            ans += remaining

        return ans


if __name__ == '__main__':
    s = "(name)is(age)yearsold"
    knowledge = [["name", "bob"], ["age", "two"]]
    print(Solution().evaluate(s, knowledge))