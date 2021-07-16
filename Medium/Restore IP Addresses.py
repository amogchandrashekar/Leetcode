from typing import List


class Solution:
    def restoreIpAddresses(self, rawIpString: str) -> List[str]:
        ans = set()

        def dfs(ind, rem, ip):
            if rem < 0:
                return

            if ind >= len(rawIpString) and rem == 0:
                nonlocal ans
                ip = ip.strip('.')
                ans.add(ip)

            updated_rem = rem - 1
            if rawIpString[ind: ind + 1]:
                dfs(ind + 1, updated_rem, ip + rawIpString[ind: ind + 1] + '.')

            if rawIpString[ind: ind + 2] and not rawIpString[ind: ind + 2].startswith('0'):
                dfs(ind + 2, updated_rem, ip + rawIpString[ind: ind + 2] + '.')

            if rawIpString[ind: ind + 3] and int(rawIpString[ind: ind + 3]) <= 255 and not rawIpString[ind: ind + 2].startswith('0'):
                dfs(ind + 3, updated_rem, ip + rawIpString[ind: ind + 3] + '.')

        dfs(0, 4, '')
        return sorted(list(ans))



if __name__ == '__main__':
    s = "125523213"
    print(Solution().restoreIpAddresses(s))