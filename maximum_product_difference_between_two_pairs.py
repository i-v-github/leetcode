"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down
the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average
(i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image,
return the image after applying the smoother on each cell of it.
"""
from typing import List
from functools import reduce

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        max_product_diff = nums_sorted[-1] * nums_sorted[-2] - nums_sorted[0] * nums_sorted[1]
        return max_product_diff




if __name__ == '__main__':
    s = Solution()
    print(s.maxProductDifference(nums = [5,6,2,7,4]))

