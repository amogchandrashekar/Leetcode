
class Solution(object):
    def buddyStrings(self, A, B):
        if (A == B):
            seen=set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs=[]
            for a,b in zip(A,B):
                if a!=b:
                    pairs.append((a,b))
            if len(pairs)>2:
                return False
            return len(pairs)==2 and pairs[0]==pairs[1][::-1]


print(Solution().buddyStrings('abc','abc'))