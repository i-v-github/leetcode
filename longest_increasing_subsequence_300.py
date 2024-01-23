"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""
from typing import List


# TODO: Solution is not correct.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1] * len(nums)
        i = 0
        for _ in range(len(nums) - 1):
            for j in range(i, len(nums) - 1):
                if nums[j+1] > nums[j]:
                    counts[i] = max(counts[i], 1 + counts[j+1])
            i += 1
        if counts:
            return max(counts)
        else:
            return 1


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS(nums = [0,1,0,3,2,3]))
    print(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
    print(s.lengthOfLIS(nums = [-2,-1]))
    print(s.lengthOfLIS(nums = [0]))
    print(s.lengthOfLIS(nums = [4,10,4,3,8,9]))