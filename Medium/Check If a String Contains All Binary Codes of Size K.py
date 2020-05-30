class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        ans = set()
        for i in range(len(s) - k + 1):
            ans.add(s[i: i + k])
        return True if len(ans) == 2 ** k else False


if __name__ == "__main__":
    s = "101111011100100110100111000110011110111101010101110011100111001001000100011101011010111000011010100101110010001" \
        "0100110011101011110001000100010101101011"
    k = 20
    print(Solution().hasAllCodes(s, k))