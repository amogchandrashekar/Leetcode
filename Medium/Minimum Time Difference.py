class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes=[]
        for timenumber in timePoints:
            minute=(int(timenumber[:2])*60)+int(timenumber[-2:])
            if minute in minutes:
                return 0
            minutes.append(minute)
        minutes.sort()
        ans=1440-minutes[-1]+minutes[0]
        for i in range(len(minutes)-1):
            if (minutes[i+1]-minutes[i])<ans:
                ans = minutes[i + 1] - minutes[i]
        return ans



print(Solution().findMinDifference(["23:59","00:00","20:54","07:18","19:24","23:57"]))
