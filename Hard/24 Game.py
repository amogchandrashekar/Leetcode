from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        if len(cards) == 1 and abs(cards[0] - 24) <= 0.001:
            return True

        for i in range(len(cards)):
            for j in range(len(cards)):
                if i == j:
                    continue

                cards_i, cards_j = cards[i], cards[j]
                base = [cards[k] for k in range(len(cards)) if k not in [i, j]]

                if self.judgePoint24(base + [cards_i + cards_j]):
                    return True

                if self.judgePoint24(base + [cards_i - cards_j]):
                    return True

                if self.judgePoint24(base + [cards_j - cards_i]):
                    return True

                if self.judgePoint24(base + [cards_i * cards_j]):
                    return True

                if cards_j != 0 and self.judgePoint24(base + [cards_i / cards_j]):
                    return True

                if cards_i != 0 and self.judgePoint24(base + [cards_j / cards_i]):
                    return True

        return False


if __name__ == '__main__':
    cards = [4, 1, 8, 7]
    print(Solution().judgePoint24(cards))