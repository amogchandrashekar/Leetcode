class Solution:
    def isValid(self, s):

        Brackets_Map={'{':'}','(':')','[':']'}
        stack=[]

        for bracket in s:
            if bracket in Brackets_Map:
                stack.append(Brackets_Map[bracket])

            elif not stack or bracket!=stack.pop():
                return False

        return not stack