from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = [[ages[i], scores[i]] for i in range(len(scores))]
        age_score.sort(key=lambda x: (x[0], x[1]))

        dp = [agescore[-1] for agescore in age_score]

        for i in range(len(age_score)):
            for j in range(i):
                if age_score[j][-1] <= age_score[i][-1]:
                    dp[i] = max(dp[i], dp[j] + age_score[i][-1])
        return max(dp) if dp else 0


if __name__ == '__main__':
    # scores = [1,2,3,5]
    # ages = [8,9,10,1]
    scores = [596, 277, 897, 622, 500, 299, 34, 536, 797, 32, 264, 948, 645, 537, 83, 589, 770]
    ages = [18, 52, 60, 79, 72, 28, 81, 33, 96, 15, 18, 5, 17, 96, 57, 72, 72]
    # scores = [9, 2, 8, 8, 2]
    # ages = [4, 1, 3, 3, 5]
    print(Solution().bestTeamScore(scores, ages))
