"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        horizontal = []
        for point in points:
            horizontal.append(point[0])
        horizontal_set = set(horizontal)
        h = list(horizontal_set)
        h.sort()
        diff = []
        for i, _ in enumerate(h):
            if i < len(h)-1:
                diff.append(h[i+1] - h[i])
        if len(diff) > 1:
            return max(diff)
        else:
            return 0



if __name__ == '__main__':
    s = Solution()
    print(s.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
    print(s.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
    print(s.maxWidthOfVerticalArea(points = [[1,1],[1,2],[1,3]]))

