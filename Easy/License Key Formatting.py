class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        dash_removed = "".join(s.split('-'))[::-1].upper()

        for ind in range(0, len(dash_removed), k):
            ans.append(dash_removed[ind: ind + k][::-1])

        return "-".join(ans[::-1])


if __name__ == '__main__':
    s = "2-5g-3-J"
    k = 2
    print(Solution().licenseKeyFormatting(s, k))