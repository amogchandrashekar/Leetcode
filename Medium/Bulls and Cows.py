from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret_counter, guess_counter = Counter(), Counter()

        for secret_char, guess_char in zip(secret, guess):

            if secret_char == guess_char:
                bulls += 1
            else:
                secret_counter[secret_char] += 1
                guess_counter[guess_char] += 1

        for char, count in secret_counter.items():
            cows += min(count, guess_counter[char])

        return f'{bulls}A{cows}B'


if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    print(Solution().getHint(secret, guess))