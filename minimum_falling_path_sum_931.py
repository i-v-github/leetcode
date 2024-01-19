"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either
directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""


def test_solution():
    s = Solution()
    assert s.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert s.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]) == -59


class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        # Initialize dp array with the first row of the matrix
        dp = matrix[0]

        # Iterate through each row starting from the second row
        for i in range(1, n):
            # Create a temporary array to store the updated dp values for the current row
            temp = [0] * n

            # Calculate the minimum falling path sum for each element in the current row
            for j in range(n):
                # Calculate the minimum value from the previous row's adjacent elements
                min_val = dp[j]
                if j > 0:
                    min_val = min(min_val, dp[j - 1])
                if j < n - 1:
                    min_val = min(min_val, dp[j + 1])

                # Update the temporary array with the minimum falling path sum for the current element
                temp[j] = matrix[i][j] + min_val

            # Update the dp array with the updated values for the current row
            dp = temp

        # Return the minimum falling path sum from the last row of the dp array
        return min(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
    assert s.minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    print(s.minFallingPathSum(matrix = [[-19,57],[-40,-5]]))
    assert s.minFallingPathSum(matrix=[[-19, 57], [-40, -5]]) == -59
