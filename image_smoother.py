"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by
rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine
cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not
consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the
image after applying the smoother on each cell of it.
"""
from typing import List
from math import floor


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smoother = []
        for i in range(len(img)):
            row = []
            for j in range(len(img[0])):
                div = 0
                summ = 0
                for k in range(max(0, i - 1), min(len(img), i + 2)):
                    for l in range(max(0, j - 1), min(len(img[0]), j + 2)):
                        cell = img[k][l]
                        summ += cell
                        div += 1
                row.append(floor(summ / div))
            smoother.append(row)
        return smoother


if __name__ == '__main__':
    s = Solution()
    # print(s.imageSmoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(s.imageSmoother(img=[[100,200,100],[200,50,200],[100,200,100]]))
