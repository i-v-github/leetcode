"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
"""
from typing import List
from functools import reduce


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = [[0,0]]
        for point in path:
            if point == 'N':
                next_point = [points[-1][0],points[-1][1] + 1]
            elif point == 'S':
                next_point = [points[-1][0], points[-1][1] - 1]
            elif point == 'E':
                next_point = [points[-1][0] + 1, points[-1][1]]
            elif point == 'W':
                next_point = [points[-1][0] - 1, points[-1][1]]
            if next_point in points:
                return True
            else:
                points.append(next_point)
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.isPathCrossing(path = "NES"))
    print(s.isPathCrossing(path = "NESWW"))

