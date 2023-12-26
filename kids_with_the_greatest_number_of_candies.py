"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for candie in candies:
            if candie + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))

