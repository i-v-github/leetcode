"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""
from itertools import zip_longest
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)
        nums_list_unique = [[i] * nums.count(i) for i in nums_set]
        transposed_list = list(map(list, zip_longest(*nums_list_unique)))
        return [list(filter(lambda x: x is not None, sublist)) for sublist in transposed_list]


if __name__ == '__main__':
    s = Solution()
    print(s.findMatrix(nums = [1,3,4,1,2,3,1]))
    print(s.findMatrix(nums = [1,2,3,4]))
