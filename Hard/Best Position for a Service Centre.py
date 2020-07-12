"""
A delivery company wants to build a new service centre in a new city.
The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a
position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map,
return the minimum sum of the euclidean distances to all customers.
"""
from typing import List
from scipy.optimize import minimize
import numpy as np


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x = [pos[0] for pos in positions]
        y = [pos[1] for pos in positions]
        x0 = np.array([sum(x) / len(x), sum(y) / len(y)])

        def dist_func(x0):
            return sum(((np.full(len(x), x0[0]) - x) ** 2 + (np.full(len(x), x0[1]) - y) ** 2) ** (1 / 2))

        res = minimize(dist_func, x0, method='nelder-mead', options={'xtol': 1e-8})
        return res.fun