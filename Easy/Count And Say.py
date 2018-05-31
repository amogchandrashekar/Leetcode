class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start='1'
        for k in range(n-1):
            letter=start[0]
            count=0
            ans=''
            for i in start:
                if i==letter:
                    count+=1
                else:
                    ans+=str(count)+letter
                    count=1
                    letter=i
            ans+=str(count)+letter
            start=ans
        
        return start
