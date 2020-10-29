"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
"""


class Solution:
	def maxDistToClosest(self, seats):
	    res, last, n = 0, -1, len(seats)
	    for i in range(n):
		if seats[i]:
		    res = max(res, i if last < 0 else (i - last) // 2)
		    last = i
	    return max(res, n - last - 1)



if __name__ == "__main__":
    seats = [1,0,0,0,1,0,1]
    print(Solution().maxDistToClosest(seats))
