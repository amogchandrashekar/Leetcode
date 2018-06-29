class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        for idx, val in enumerate(list1):
            dict1[val] = idx

        idx_sum = len(list1) + len(list2) - 2
        res = []
        for idx, val in enumerate(list2):
            if val in dict1:
                if idx + dict1[val] == idx_sum:
                    res.append(val)
                elif idx + dict1[val] < idx_sum:
                    idx_sum = idx + dict1[val]
                    res = []
                    res.append(val)
        return res

print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC","amog"],["Piatti", "The Grill at Torrey Pines","Tapioca Express", "Hungry Hunter Steakhouse", "Shogun"]))