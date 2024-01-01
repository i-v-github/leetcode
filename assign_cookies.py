"""Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for cookie in s:
            for child in g:
                if cookie >= child:
                    i += 1
                    g.pop(g.index(child))
                    break
        return i




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren(g = [1,2,3], s = [1,1]))
    print(s.findContentChildren(g = [1,2,3], s = [3]))
